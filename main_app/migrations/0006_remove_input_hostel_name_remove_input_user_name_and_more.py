# Generated by Django 4.0.4 on 2022-05-25 17:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_input_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='hostel_name',
        ),
        migrations.RemoveField(
            model_name='input',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='input',
            name='rating',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
