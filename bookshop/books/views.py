from django.shortcuts import render
from rest_framework import generics
from .models import Books, Profiles
from .serializer import BookSerializer, ProfileSerializer

# Create your views here.
class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfileSerializer

class ProfileVisibleFalse(generics.ListCreateAPIView):
    queryset = Profiles.objects.filter(is_visible=False)
    serializer_class = ProfileSerializer

class ProfileVisibleTrue(generics.ListCreateAPIView):
    queryset = Profiles.objects.filter(is_visible=True)
    serializer_class = ProfileSerializer

class ProfileRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfileSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
