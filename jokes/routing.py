from django.urls import path
from .consumers import JokesConsumer
ws_urlpatterns = [
    path('ws/jokes/', JokesConsumer.as_asgi()),
]
