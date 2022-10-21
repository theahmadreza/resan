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
    peoples = User.objects.all()
    context = {
        "peoples": peoples
    }

    return render(request, 'chat/index.html', context)
   
   
   
# for send users id use 'pk'
def chat_page(request, pk):
    peoples = Users.objects.all()
    people = None

    print(peoples)

    """
    for make users chat available on chat page 
        - create loop for peoples dict (temporary)
        - check if people id's equal by primary key\
            then people variable equel by people who\
            theres id equal by primary key
    """
    for i in peoples:
        if i['id'] == int(pk):
            people = i
    
    context = {
        "people": people,
        # "users": Users.objects.all() #temporary
    }
    
    
    return render(request, 'chat/chat_page.html', context)