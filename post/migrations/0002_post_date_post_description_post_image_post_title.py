# Generated by Django 5.0.6 on 2024-05-23 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='post/images'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
