from django.db import models
from ckeditor.fields import RichTextField


class Generator(models.Model):
    doctext = RichTextField(blank=True, null=True)
