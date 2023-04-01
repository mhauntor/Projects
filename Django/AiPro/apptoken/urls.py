from apptest import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MyTokenObtainPairView
urlpatterns = [
    path('api/token/login/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token2/', MyTokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    
]
