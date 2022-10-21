from django.shortcuts import render
from .models import *


from django.contrib.auth.models import User
# Create your views here.

"""
peoples = [
    {
        'id': 1,
        'name': '@amir'
    }, 
    {
        'id': 2,
        'name': '@ali'
    },
    {
        'id': 3,
        'name': '@amin'
    },
]
"""


def index(request):
    peoples = Users.objects.all()

    context = {
        "peoples": peoples
    }
    return render(request, 'chat/index.html', context)
   
   
   
# for send users id use 'pk'
def chat_page(request, pk):
    peoples = Users.objects.get(id=pk)

    context = {
        "peoples": peoples
    }
    return render(request, 'chat/chatPage.html', context)