from django.shortcuts import render
from .serializers import RoomSerializer
from .models import Room
from rest_framework import generics


# Create your views here.
from django.http import HttpResponse
def main(request):
    return HttpResponse("Hello World")

class RoomView(generics.ListAPIView): # CreateAPIView to post
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
