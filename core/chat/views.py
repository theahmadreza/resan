from django.shortcuts import render

# Create your views here.

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


def index(request):
    context = {
        "peoples": peoples
    }

    return render(request, 'chat/index.html', context)
   
   
   
# for send users id use 'pk'
def chat_page(request, pk):
    people = None

    for i in peoples:
        if i['id'] == int(pk):
            people = i
    
    context = {
        "people": people
    }
    
    
    return render(request, 'chat/chat_page.html', context)