from rest_framework import serializers
from .models import user2

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = user2
        fields = ['guuid', 'email', 'first_name', 'last_name', 'phone_number', 'image_url', 'address','password']


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = user2
        fields = ('email', 'password')