# Generated by Django 5.0.1 on 2024-03-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogWebApp', '0017_alter_blogentry_date_of_creation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogentry',
            options={'verbose_name': 'Blog Entry', 'verbose_name_plural': 'Blog Entries'},
        ),
        migrations.AddField(
            model_name='blogentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/', verbose_name='Image'),
        ),
    ]
