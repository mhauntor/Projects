from django.contrib import admin

# Register your models here.
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone_number', 'image_url', 'address']

admin.site.register(Client, ClientAdmin)