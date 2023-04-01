from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .serializers import ClientSerializer, PhoneSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Client,Phone
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings


# Create your views here.
@api_view(['POST'])
#@permission_classes(['AllowAny',])
def register_client(request):
    serializer = ClientSerializer(data=request.data)
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
        client = Client.objects.get(email=email)
    except Client.DoesNotExist:
        return Response({'error': 'Invalid email or password'})

    if not check_password(password, client.password):
        return Response({'error': 'Invalid email or password'})

    
    refresh = RefreshToken.for_user(client)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)


    
    serializer = ClientSerializer(client)
    data = serializer.data
    data['access'] = access_token
    data['refesh'] = refresh_token
    return Response(data)


    '''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def phone_list(request):
    # retrieve the token from the Authorization header
    access_token = request.headers.get('Authorization').split()[1]

    phones = Phone.objects.all()
    serializer = PhoneSerializer(phones, many=True)

    # add the access_token to the response headers
    response = Response(serializer.data)
    response['Authorization'] = 'Bearer' + access_token
    return response'''