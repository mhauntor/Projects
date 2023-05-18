from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Client4
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
#class Client4Serializer(serializers.ModelSerializer):
class Client4Serializer(TokenObtainPairSerializer):
    password = serializers.CharField(write_only=True, required=True, max_length=128)

    class Meta:
        model = Client4
        fields = ('guuid', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'image_url', 'address')
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    