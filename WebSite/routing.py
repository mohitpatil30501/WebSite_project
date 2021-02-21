from django.urls import path

from User import consumers

websocket_urlpatterns = [
    path('user/<str:id>', consumers.UserConsumer.as_asgi()),
    path('user/reset_password/<str:id>', consumers.UserResetPasswordConsumer.as_asgi()),
]
