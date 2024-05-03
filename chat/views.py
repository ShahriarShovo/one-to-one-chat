from django.shortcuts import render

# Create your views here.

def chat_index(request):
    return render(request, 'chat/chat_room.html')

def conversation(request,pk):
    
    return render(request, 'chat/message_body.html')
