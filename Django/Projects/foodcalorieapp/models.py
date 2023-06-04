from django.db import models

class FoodChart(models.Model):
    food_name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    calorie = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    fats = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.food_name