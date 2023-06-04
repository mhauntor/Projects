import os
import django
from django.db import connection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Projects.Projects.settings.py")
django.setup()

def add_datasql():
    with connection.cursor() as cursor:
        # Write your SQL command to insert data
        sql = """
        INSERT INTO foodcalorieapp_foodchart (food_name, weight, calorie, protein, fats, carbohydrates)
        VALUES ('Apple', 100, 52.0, 0.3, 0.2, 14.0),
               ('Banana', 120, 96.0, 1.2, 0.3, 25.0),
               ('Chicken Breast', 150, 165.0, 31.0, 3.6, 0.5);
        """
        cursor.execute(sql)

add_datasql()