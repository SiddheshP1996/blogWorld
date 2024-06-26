# Generated by Django 5.0.1 on 2024-03-26 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogWebApp', '0014_alter_blogentry_date_of_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2024, 3, 26, 19, 55, 58, 510323, tzinfo=datetime.timezone.utc), verbose_name='Date of Creation'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 26, 19, 55, 58, 500319, tzinfo=datetime.timezone.utc), verbose_name='Created At'),
        ),
    ]
