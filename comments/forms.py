from django import forms
from captcha.fields import CaptchaField
from comments.models import Comment


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = [
            "user_name",
            "email",
            "home_page",
            "text",
            "parent_comment"
        ]
        labels = {
            "user_name": "User Name",
            "email": "E-mail",
            "home_page": "Home Page",
            "text": "Text",
            "parent_comment": "Parent Comment"
        }
        help_texts = {
            "parent_comment": "Select parent comment (optional)"
        }
