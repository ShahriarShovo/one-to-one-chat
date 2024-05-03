from django.urls import path
from chat.views import conversation


urlpatterns = [
    path('', conversation, name='conversation')
]
