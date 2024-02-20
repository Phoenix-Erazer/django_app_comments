from django.urls import path
from .views import CommentListView, add_comment, home

urlpatterns = [
    path("add/", add_comment, name="add_comment"),
    path("comment-list/", CommentListView.as_view(), name="comment_list"),
    path("", home, name="home"),
]

app_name = "comments"
