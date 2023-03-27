from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app2reg import views


urlpatterns = [
    path('api/registration/', views.user_registration, name='registration'),
    path('api/login/', views.login, name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
