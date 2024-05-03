from django.urls import path
from chat.views import chat_index, conversation

urlpatterns = [
    path('home/', chat_index, name='chat_index'),
    path('home/conversation/<int:pk>', conversation, name='conversation'),
]
