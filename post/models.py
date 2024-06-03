from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

class post(models.Model):
    title = CharField(max_length=100, default=None)
    description = CharField(max_length=256, default=None)
    author = CharField(max_length=100, default=None)
    image = ImageField(upload_to="post/images", default=None)
    url = URLField(blank=True)
    date = DateField(default=date.today)

    def __str__(self) -> str:
        return self.title