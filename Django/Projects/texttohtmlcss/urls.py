# urls.py

from django.urls import path
from texttohtmlcss import views

urlpatterns = [
    path('', views.textToHtml, name='generator'),
]
