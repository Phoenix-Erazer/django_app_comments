from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import generic

from .models import Comment
from .forms import CommentForm


def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comments:home")
    else:
        form = CommentForm()
    return render(request, "includes/add_comment.html", {"form": form})


class CommentListView(generic.ListView):
    model = Comment
    template_name = "includes/comment_list.html"
    context_object_name = "comment_list"
    paginate_by = 25

    queryset = Comment.objects.select_related("user").order_by("-created_at")


def home(request):
    comments = Comment.objects.filter(parent_comment__isnull=True).order_by(
        "-created_at"
    )
    paginator = Paginator(comments, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "comments/home.html", {"page_obj": page_obj})
