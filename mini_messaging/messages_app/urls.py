from django.urls import path
from messages_app import views

urlpatterns = [
    path("messages/", views.get_messages),
    path("send/", views.send_message),
]
