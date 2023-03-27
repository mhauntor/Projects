from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Client3

class Client3Serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, max_length=128)

    class Meta:
        model = Client3
        fields = ('guuid', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'image_url', 'address')
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
