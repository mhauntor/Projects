# Generated by Django 4.1.7 on 2023-03-26 03:58

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app2reg', '0002_alter_user1_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Example: +8801XXXXXXXXX', max_length=14, region='BD'),
        ),
    ]
