from django.db import models
from django.core.validators import RegexValidator, URLValidator, EmailValidator


class Comment(models.Model):
    alphanumeric_validator = RegexValidator(
        regex=r"^[0-9a-zA-Z]*$",
        message="Only alphanumeric characters are allowed."
    )
    email_validator = EmailValidator()
    url_validator = URLValidator()

    user_name = models.CharField(
        max_length=100,
        validators=[alphanumeric_validator]
    )
    email = models.EmailField(validators=[email_validator])
    home_page = models.URLField(
        blank=True, null=True,
        validators=[url_validator]
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True,
        related_name="comments"
    )

    def __str__(self):
        return (
            f"{self.user_name}({self.created_at}): "
            f"{self.text}"
        )
