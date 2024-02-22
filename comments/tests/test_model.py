from django.test import TestCase
from django.contrib import admin
from comments.admin import CommentAdmin
from comments.models import Comment


class AdminTests(TestCase):
    def setUp(self) -> None:
        self.comment_admin = CommentAdmin
        self.comment_model_admin = admin.site._registry[Comment]

    def test_comment_admin_should_be_registered(self):
        self.assertTrue(isinstance(self.comment_model_admin, self.comment_admin))

    def test_comment_admin_list_display(self):
        expected_list_display = ["user_name", "email", "text", "created_at", "parent_comment"]
        self.assertEqual(self.comment_admin.list_display, expected_list_display)

    def test_comment_admin_list_filter(self):
        expected_list_filter = ["user_name", "created_at"]
        self.assertEqual(self.comment_admin.list_filter, expected_list_filter)

    def test_comment_admin_search_fields(self):
        expected_search_fields = ["user_name"]
        self.assertEqual(self.comment_admin.search_fields, expected_search_fields)
