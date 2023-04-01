from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import Client4Serializer
from .models import Client4,Token, ClientBearerToken
from django.contrib.auth.hashers import check_password
import datetime
from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings

@api_view(['POST'])
#@permission_classes(['AllowAny',])
def register_client(request):
    serializer = Client4Serializer(data=request.data)
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
        client = Client4.objects.get(email=email)
    except Client4.DoesNotExist:
        return Response({'error': 'Invalid email or password'})

    if not check_password(password, client.password):
        return Response({'error': 'Invalid email or password'})

    '''client_token = ClientBearerToken.objects.filter(client=client).first()

    if client_token and client_token.expires_at > timezone.now():
        token = client_token.token
        expires_at = client_token.expires_at
    else:'''
    
    token = ClientBearerToken.objects.create(client=client).token
    expires_at = (timezone.now() + datetime.timedelta(days=2))



    
    serializer = Client4Serializer(client)
    data = serializer.data
    data['token'] = token
    data['expires_at'] = expires_at
    return Response(data)

'''
from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Client3

def generate_bearer_token(client: Client3) -> str:
    refresh = RefreshToken.for_user(client)
    refresh.set_exp(lifetime=timedelta(days=2))
    return str(refresh.access_token)

'''

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = Client4Serializer