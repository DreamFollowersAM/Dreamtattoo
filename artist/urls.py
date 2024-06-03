from django.urls import path
from . import views

app_name = 'artist'

urlpatterns = [
    path("", views.renderArtist, name="Artist"),
    path("<str:art_username>", views.artist_detail, name="artist_detail"),
]