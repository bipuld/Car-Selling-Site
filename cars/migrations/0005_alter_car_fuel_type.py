# Generated by Django 4.1.3 on 2023-01-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_features_alter_car_vin_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('diesel', 'diesel'), ('petrol', 'petrol'), ('hybrid', 'hybrid')], max_length=50),
        ),
    ]
