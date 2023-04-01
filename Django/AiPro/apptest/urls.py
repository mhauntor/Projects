from apptest import views
from django.urls import path, include
from .views import MyTokenObtainPairView


urlpatterns = [
    path('api/registration/', views.register_client, name='registration'),
    path('api/login/', views.login, name='login'),
    path('api/ln/', MyTokenObtainPairView.as_view(), name='login'),
    
]
