# Generated by Django 5.0.1 on 2024-02-25 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogWebApp', '0005_alter_fileattachment_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FileAttachment',
        ),
    ]
