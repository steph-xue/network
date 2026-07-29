from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Extends Django's built-in user model
class User(AbstractUser):
    pass


# A single post made by a user
class Post(models.Model):
    content = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    date_time = models.DateTimeField(auto_now_add=True)

    # Returns a readable description of the post, its author, and when it was posted
    def __str__(self):
        return f"Post {self.id} was posted by {self.user.username.capitalize()} on {self.date_time.strftime('%m/%d/%Y, %H:%M:%S')}"


# Records that one user follows another user
class Follow(models.Model):
    user_follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower_user")
    user_following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following_user")

    # Returns a readable description of the follow relationship
    def __str__(self):
        return f"{self.user_follower.username.capitalize()} is now following {self.user_following.username.capitalize()}"


# Records that a user liked a post
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like_post")

    # Returns a readable description of the like
    def __str__(self):
        return f"{self.user.username.capitalize()} liked post {self.post.id}"


# Records that a user disliked a post
class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dislike_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="dislike_post")

    # Returns a readable description of the dislike
    def __str__(self):
        return f"{self.user.username.capitalize()} disliked post {self.post.id}"
