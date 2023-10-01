# Generated by Django 4.1.3 on 2023-01-14 17:42

import ckeditor.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_doors_alter_car_fuel_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=20),
        ),
    ]