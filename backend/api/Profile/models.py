from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.id, filename)
class UserProfile(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return self.username
class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['user', '-timestamp']),
            models.Index(fields=['-likes']),
            models.Index(fields=['-comments']),
        ]

class Follower(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        indexes = [
            models.Index(fields=['user', 'follower']),
        ]
        unique_together = ['user', 'follower']

# class Message(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     api = models.ForeignKey(API, on_delete=models.CASCADE)
#     content = models.TextField()
#     source = models.CharField(max_length=50)
#     timestamp = models.DateTimeField()

#     class Meta:
#         indexes = [
#             models.Index(fields=['user', '-timestamp']),
#         ]