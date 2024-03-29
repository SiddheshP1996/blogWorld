# Generated by Django 5.0.1 on 2024-02-25 20:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogWebApp', '0008_alter_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='date_of_creation',
            field=models.DateField(auto_now_add=True, verbose_name='Date of Creation'),
        ),
    ]
