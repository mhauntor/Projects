from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Client3Serializer
from .models import Client3,Token, ClientBearerToken
from django.contrib.auth.hashers import check_password
import datetime
from django.utils import timezone
@api_view(['POST'])
def register_client(request):
    serializer = Client3Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Please provide both email and password'})

    try:
        client = Client3.objects.get(email=email)
    except Client3.DoesNotExist:
        return Response({'error': 'Invalid email or password'})

    if not check_password(password, client.password):
        return Response({'error': 'Invalid email or password'})

    #token, created = Token.objects.get_or_create(client=client)
    #token = ClientBearerToken.objects.create(client=client).token
    #expires_at = (datetime.datetime.now() + datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')
    client_token = ClientBearerToken.objects.filter(client=client).first()

    if client_token and client_token.expires_at > timezone.now():
        token = client_token.token
        expires_at = client_token.expires_at
    else:
        token = ClientBearerToken.objects.create(client=client).token
        expires_at = (timezone.now() + datetime.timedelta(days=2))




    
    serializer = Client3Serializer(client)
    data = serializer.data
    data['bearer_token'] = token
    data['expires_at'] = expires_at
    return Response(data)