# Generated by Django 4.2.1 on 2023-05-22 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('texttohtmlcss', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generator',
            old_name='rt',
            new_name='doctext',
        ),
    ]
