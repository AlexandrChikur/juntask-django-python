# Generated by Django 3.1.4 on 2020-12-18 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_personal_cars'),
        ('cars', '0002_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='personal_cars', to='users.user'),
        ),
    ]
