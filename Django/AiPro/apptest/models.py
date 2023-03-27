import uuid
from django.db import models

    
class Client3(models.Model):
    guuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=60)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"









class Client2(models.Model):
    guuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=60)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"