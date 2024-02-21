from django.urls import path
from .views import CommentListView, CommentCreateView

urlpatterns = [
    path("add/", CommentCreateView.as_view(), name="add_comment"),
    path("comment-list/", CommentListView.as_view(), name="comment_list"),
]

app_name = "comments"
