from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Users(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    userName = models.CharField(max_length=10)
    UserPic = models.ImageField(upload_to="static/Users/pics")
    # email =

    def __str__(self):
        return f"user: '{self.user}', username:'{self.userName}'"


class Chat(models.Model):
    # for now(temporary) users can only send a image
    user = models.ForeignKey(
        User, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to="static/Users/send_images")
    message = models.CharField(max_length=64)   
    sendTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} send {self.message}"