from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db.models import Prefetch


from .forms import CommentForm
from .models import Comment


@login_required  # Add a decorator to require authentication
def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            parent_comment = form.cleaned_data["parent_comment"]
            user = request.user  # Use an authenticated user
            comment = Comment(
                user=user,
                text=text,
                parent_comment=parent_comment
            )
            comment.save()
            return redirect("comments:home")
    else:
        # Use the registered user data to fill out the form
        initial_data = {
            "username": request.user.username,
            "email": request.user.email
        }
        form = CommentForm(initial=initial_data)
    return render(request, "includes/add_comment.html", {"form": form})


class CommentListView(generic.ListView):
    model = Comment
    template_name = "includes/comment_list.html"
    context_object_name = "comment_list"
    paginate_by = 25

    queryset = Comment.objects.select_related('user').order_by("-created_at")


def home(request):
    comments = Comment.objects.select_related('user').order_by("-created_at")

    current_user = request.user if request.user.is_authenticated else None

    form = CommentForm(
        initial={
            "username": current_user.username if current_user else "",
            "email": current_user.email if current_user else "",
        }
    )

    return render(
        request, "comments/home.html",
        {"comments": comments,
         "form": form}
    )
