from django.shortcuts import render
from rest_framework.decorators import api_view
from messages_app.serializers import MessageSerializer
from rest_framework.response import Response
from messages_app.models import Message

@api_view(["GET"])
def get_messages(request):
    messages = Message.objects.all().order_by("-timestamp")
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def send_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Message sent successfully!"})
