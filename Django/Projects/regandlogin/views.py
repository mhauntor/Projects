from rest_framework.decorators import api_view
from .serializers import ClientSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings


# registration form view.
@api_view(['POST'])
#@permission_classes(['AllowAny',])
def registration(request):
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
        return Response({'error': 'Invalid email '})

    if not check_password(password, client.password):
        return Response({'error': 'Invalid password'})

    
    refresh = RefreshToken.for_user(client)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)


    
    serializer = ClientSerializer(client)
    data = serializer.data
    data['access'] = access_token
    data['refesh'] = refresh_token
    return Response(data)