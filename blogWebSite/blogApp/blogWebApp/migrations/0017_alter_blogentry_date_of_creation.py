# Generated by Django 5.0.1 on 2024-03-26 19:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogWebApp', '0016_alter_blogentry_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='date_of_creation',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date of Creation'),
        ),
    ]
