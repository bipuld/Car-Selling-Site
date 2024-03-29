# Generated by Django 4.2.4 on 2023-10-17 06:48

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_team_facebook_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('message', ckeditor.fields.RichTextField()),
                ('contact_date', models.DateTimeField(default=datetime.datetime(2023, 10, 17, 12, 33, 7, 138192))),
            ],
        ),
    ]
