from regandlogin import views
from django.urls import path

urlpatterns = [
    path('reg/', views.registration,name='registration'),
    path('login/', views.login,name='login'),
    
    
]
