from django.urls import reverse_lazy
from django.views import generic

from .models import Comment
from .forms import CommentForm


class CommentCreateView(generic.CreateView):
    form_class = CommentForm
    success_url = reverse_lazy("comments:comment_list")
    template_name = "comments/add_comment.html"


class CommentListView(generic.ListView):
    model = Comment
    template_name = "comments/comment_list.html"
    context_object_name = "comment_list"
    paginate_by = 25

    queryset = Comment.objects.filter(
        parent_comment__isnull=True
    ).prefetch_related(
        "__".join(["comments"] * 10)).order_by("created_at")
