# Generated by Django 4.0.4 on 2022-05-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_input_hostel_name_remove_input_user_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='country',
            field=models.CharField(default='Paris', max_length=100),
            preserve_default=False,
        ),
    ]