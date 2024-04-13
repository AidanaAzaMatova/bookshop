from rest_framework import serializers
from .models import Books, Profiles

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('id', 'column_name', 'is_visible')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'name', 'author', 'price')