from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.contrib.auth.hashers import make_password

def user_image_path(instance, filename):
    return f"images/user_{instance.guuid}/{filename}"

# Create your models here.
class user1(models.Model):
    guuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=60)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(region='BD', max_length=14, help_text='Example: +8801XXXXXXXXX')
    image_url = models.URLField(max_length=255)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=128, null=False)
    def __str__(self):
        return self.first_name + " " + self.last_name


class user3(models.Model):
    guuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=60)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(region='BD', max_length=14, help_text='Example: +8801XXXXXXXXX')
    image_url = models.URLField(max_length=255)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=128, null=False)
    def __str__(self):
        return self.first_name + " " + self.last_name


class user2(models.Model):
    guuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=60)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(region='BD', max_length=14, help_text='Example: +8801XXXXXXXXX')
    image_url = models.URLField(max_length=255)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.first_name + " " + self.last_name