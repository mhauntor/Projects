from apptest import views
from django.urls import path, include


urlpatterns = [
    path('api/registration/', views.register_client, name='registration'),
    path('api/login/', views.login, name='login'),
    #path('api/login/', views.login, name='login'),
]
