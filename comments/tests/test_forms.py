from captcha.fields import CaptchaField
from django.test import TestCase
from comments.forms import CommentForm
from comments.models import Comment


class CommentFormTests(TestCase):
    def setUp(self):
        self.form = CommentForm()

    def test_form_model(self):
        self.assertEqual(self.form.Meta.model, Comment)

    def test_form_fields(self):
        expected_fields = ["user_name", "email", "home_page", "text", "parent_comment"]
        self.assertEqual(list(self.form.Meta.fields), expected_fields)

    def test_form_field_labels(self):
        field_labels = {
            "user_name": "User Name",
            "email": "E-mail",
            "home_page": "Home Page",
            "text": "Text",
            "parent_comment": "Parent Comment"
        }
        for field_name, expected_label in field_labels.items():
            with self.subTest(field_name=field_name):
                self.assertEqual(self.form.fields[field_name].label, expected_label)

    def test_form_field_help_text(self):
        self.assertEqual(self.form.fields["parent_comment"].help_text, "Select parent comment (optional)")

    def test_captcha_field(self):
        self.assertTrue(isinstance(self.form.fields["captcha"], CaptchaField))
