from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
            comment = Comment(user=user, text=text, parent_comment=parent_comment)
            comment.save()
            return redirect("comments:home")
    else:
        # Use the registered user data to fill out the form
        initial_data = {"username": request.user.username, "email": request.user.email}
        form = CommentForm(initial=initial_data)
    return render(request, "add_comment.html", {"form": form})


def comment_list(request: HttpRequest) -> HttpRequest:
    comments = Comment.objects.all()
    return render(request, "comment_list.html", {"comments": comments})


def home(request):
    # Get all comments sorted by date added in descending order (LIFO)
    comments = Comment.objects.order_by("-created_at")

    # Разбиваем комментарии на страницы по 25 сообщений на каждой
    page_number = request.GET.get("page", 1)
    paginator = Paginator(comments, 25)
    page_obj = paginator.get_page(page_number)

    # Получаем текущего аутентифицированного пользователя
    current_user = request.user if request.user.is_authenticated else None

    # Передаем текущего пользователя в форму
    form = CommentForm(
        initial={
            "username": current_user.username if current_user else "",
            "email": current_user.email if current_user else "",
        }
    )

    return render(request, "home.html", {"page_obj": page_obj, "form": form})
