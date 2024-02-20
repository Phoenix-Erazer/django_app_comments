from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "user_name",
        "email",
        "text",
        "created_at",
        "parent_comment",
    ]
    list_filter = [
        "user_name",
        "created_at",
    ]
    search_fields = [
        "user_name",
    ]
