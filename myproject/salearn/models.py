from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=10)


class LecturePortal(models.Model):
    """
    creating a lecture model to handle all the attributes that the lecture's view contains
    """

    pass

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    length = models.DurationField()
    video_file = models.FileField(upload_to="videos/")
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s comment on {self.video.title}"
    