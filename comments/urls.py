from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_comment, name="add_comment"),
    path("comment-list/", views.comment_list, name="comment_list"),
    path("", views.home, name="home"),
]

app_name = "comments"
