from . import views
#from . views import PhoneList
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#from .views import MyTokenObtainPairView
urlpatterns = [
    path('a/', views.register_client,name='registration'),
    path('b/', views.login,name='login'),
    #path('c/', views.phone_list,name= 'catalog'),
    #path('', MyTokenObtainPairView.as_view()),
    #path('c/', TokenRefreshView.as_view()),
    
]
