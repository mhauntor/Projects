from django.shortcuts import render
from .models import FoodChart

def calculate(request):
    food_list = FoodChart.objects.all()
    context = {'food_list': food_list}
    return render(request, 'foods/food.html', context)