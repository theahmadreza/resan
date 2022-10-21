from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Users(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    userName = models.CharField(max_length="10")
    UserPic = models.ImageField(upload_to="static/Users/pics")
    # email =


class Chat(models.Model):
    # for now(temporary) users can only send a image
    image = models.ImageField(upload_to="static/Users/send_images")
    messages = models.CharField(max_length="64")   
    sendTime = models.DateTimeField(auto_now_add=True)