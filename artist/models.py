from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

class artist(models.Model):
    name = CharField(max_length=100, default=None)
    description = CharField(max_length=256, default=None)
    username = CharField(max_length=100, default=None)
    image = ImageField(upload_to="artist/images", default=None)
    instagram = URLField(blank=True)
    youtube = URLField(blank=True)
    other = URLField(blank=True)

    def __str__(self) -> str:
        return self.name