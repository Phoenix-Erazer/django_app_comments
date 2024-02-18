from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from comments.models import Comment, User


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "text", "created_at", "parent_comment", ]
    list_filter = ["user", "created_at", ]
    search_fields = ["user__username", ]


admin.site.register(User, UserAdmin)
