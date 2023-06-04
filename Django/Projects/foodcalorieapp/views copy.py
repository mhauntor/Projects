from decimal import Decimal, ROUND_DOWN
from django.shortcuts import render
from foodcalorieapp.models import FoodChart

def calculate(request):
    form = FoodSelectionForm()
    if request.method == 'POST':
        selectfood = request.POST.get('select_query', '')
        if selectfood:
            food = FoodChart.objects.filter(food_name__icontains=selectfood).first()
            if food:
                selected_foods = request.session.get('selected_foods', [])
                selected_foods.append(food.id)
                request.session['selected_foods'] = selected_foods
    
    selected_foods = FoodChart.objects.filter(id__in=request.session.get('selected_foods', []))
    total_carbohydrate = sum(float(food.carbohydrates) for food in selected_foods)
    total_carbohydrate = Decimal(total_carbohydrate).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
    context = {
        'form': form,
        'all_foods': FoodChart.objects.all()
    }
    context2 = {
        'selected_foods': selected_foods,
        'total_carbohydrate': total_carbohydrate,
    }




    '''
    if request.method == 'POST':
        selectfood = request.POST.get('search_query', '')
        if selectfood:
            food = FoodChart.objects.filter(food_name__icontains=selectfood).first()
            if food:
                selected_foods = request.session.get('selected_foods', [])
                selected_foods.append(food.id)
                request.session['selected_foods'] = selected_foods

    selected_foods = FoodChart.objects.filter(id__in=request.session.get('selected_foods', []))
    total_carbohydrate = sum(float(food.carbohydrates) for food in selected_foods)

    # Convert total_carbohydrate to Decimal if needed
    total_carbohydrate = Decimal(total_carbohydrate).quantize(Decimal('0.00'), rounding=ROUND_DOWN)

    context = {
        'selected_foods': selected_foods,
        'total_carbohydrate': total_carbohydrate,
    }'''
    return render(request, 'foods/calculate.html', context,context2)


from django.shortcuts import render
from .forms import FoodSelectionForm
from .models import FoodChart

def food_chart(request):
    '''all_foods = FoodChart.objects.all()

    context = {
        'all_foods': all_foods
    }

    return render(request, 'foods/food_chart.html', context)'''
    form = FoodSelectionForm()

    if request.method == 'POST':
        form = FoodSelectionForm(request.POST)
        if form.is_valid():
            selected_food = form.cleaned_data['food']
            # Process the selected food as needed

    context = {
        'form': form,
        'all_foods': FoodChart.objects.all()
    }

    return render(request, 'foods/food_chart.html', context)
