from django.urls import path

from User import consumers

websocket_urlpatterns = [
    path('user/<str:id>', consumers.UserConsumer.as_asgi()),
]
