from django.urls import path
from .views import CommentListView, home, CommentCreateView

urlpatterns = [
    path("add/", CommentCreateView.as_view(), name="add_comment"),
    path("comment-list/", CommentListView.as_view(), name="comment_list"),
    path("", home, name="home"),
]

app_name = "comments"
