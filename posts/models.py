from django.db import models
from django.core.validators import MinLengthValidator


class User(models.Model):
    username = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(3)],
    )
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    content = models.TextField(validators=[MinLengthValidator(1)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]
