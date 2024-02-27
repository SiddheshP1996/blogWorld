# Generated by Django 5.0.1 on 2024-02-25 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogWebApp', '0003_blogentry_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='blog_attachments', verbose_name='File')),
                ('blog_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_attachments', to='blogWebApp.blogentry')),
            ],
        ),
    ]