from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from .models import Client,Phone

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
#class Client4Serializer(TokenObtainPairSerializer):
    password = serializers.CharField(write_only=True, required=True, max_length=128)

    class Meta:
        model = Client
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'image_url', 'address')
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


