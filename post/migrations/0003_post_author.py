# Generated by Django 5.0.6 on 2024-05-24 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_date_post_description_post_image_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=None, max_length=100),
        ),
    ]