# Generated by Django 4.1.7 on 2023-03-26 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2reg', '0003_alter_user1_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user1',
            name='password',
            field=models.CharField(default=1, help_text='Enter password', max_length=128),
            preserve_default=False,
        ),
    ]
