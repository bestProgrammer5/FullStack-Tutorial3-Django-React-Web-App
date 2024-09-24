from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]

        extra_kwargs = {"password": {"write_only": True}}
        #We will not return the password, when we are giving the information about the user. No one can read what the password is.
        #Password will be only accepted, when the user will create a password. 

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}