# urls.py

from django.urls import path
from calculatorapp import views

urlpatterns = [
    path('', views.calculator_view, name='calculator'),
]
