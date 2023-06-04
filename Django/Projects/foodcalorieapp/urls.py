# urls.py

from django.urls import path
from foodcalorieapp import views

urlpatterns = [
    path('', views.calculate, name='calculator'),
]
