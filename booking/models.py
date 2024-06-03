from django.db import models
from django.db.models.fields import CharField, DateTimeField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

class booking(models.Model):
    title = CharField(max_length=100, default=None)
    description = CharField(max_length=256, default=None)
    artist = CharField(max_length=100, default=None)
    date = DateTimeField(default=None)

    def __str__(self) -> str:
        return self.title