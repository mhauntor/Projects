# Generated by Django 4.1.7 on 2023-04-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiauth', '0003_rename_guuid_client_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('ramsize', models.CharField(max_length=20)),
                ('romsize', models.CharField(max_length=20)),
            ],
        ),
    ]
