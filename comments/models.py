from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models


class User(AbstractUser):
    homepage = models.URLField(blank=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user}: {self.text}"
