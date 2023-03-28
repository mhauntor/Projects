import uuid
from django.db import models
import datetime
    
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



class ClientBearerToken(models.Model):
    client = models.ForeignKey('Client3', on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.expires_at = datetime.datetime.now() + datetime.timedelta(days=30)
        super().save(*args, **kwargs)

    def is_expired(self):
        return datetime.datetime.now() > self.expires_at

class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    client = models.ForeignKey(Client3, related_name='auth_token', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)







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