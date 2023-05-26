from django.db import models
    
class foods(models.Model):
    Food =models.CharField(max_length=128)
    Calories = models.IntegerField(blank =True, null =True)
    Total_Fat = models.IntegerField(blank =True, null =True)
    Sodium = models.IntegerField(blank =True, null =True)
    Potassium = models.IntegerField(blank =True, null =True)
    Total_Carbohydrate = models.IntegerField(blank =True, null =True)
    Dietary_Fiber = models.IntegerField(blank =True, null =True)
    Protein = models.IntegerField(blank =True, null =True)
    Vitamin_A = models.IntegerField(blank =True, null =True)
    Vitamin_C = models.IntegerField(blank =True, null =True)
    Calcium = models.IntegerField(blank =True, null =True)  


    def __str__(self):
        return f"{self.Food}"