from django.db import models
<<<<<<< HEAD
from django.core.validators import MinLengthValidator


class User(models.Model):
    username = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(3)],
    )
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
=======

# Define the models - L.Llanto

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)  # User's unique username
    email = models.EmailField(unique=True)  # User's unique email
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the user was created

>>>>>>> main

    def __str__(self):
        return self.username


class Post(models.Model):
<<<<<<< HEAD
    content = models.TextField(validators=[MinLengthValidator(1)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]
=======
    content = models.TextField()  # The text content of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who created the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post was created


    def __str__(self):
         return f"Post by {self.author.username} at {self.created_at}"

    
class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.id}"



>>>>>>> main
