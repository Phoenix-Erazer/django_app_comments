from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField

from comments.models import Comment


class CommentForm(forms.Form):
    username = forms.CharField(
        label="User Name",
        max_length=50,
        required=True,
        help_text="Only letters and digits are allowed.",
    )
    email = forms.EmailField(label="E-mail", required=True)
    homepage = forms.URLField(label="Home page", required=False)
    captcha = CaptchaField()
    text = forms.CharField(label="Text", widget=forms.Textarea, required=True)
    parent_comment = forms.ModelChoiceField(
        queryset=Comment.objects.select_related('user').order_by("-created_at"),
        required=False,
        empty_label="Select parent comment (optional)",
    )
