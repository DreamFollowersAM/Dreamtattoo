from django.shortcuts import render, get_object_or_404
from .models import artist
from post.models import post
from booking.models import booking
from datetime import date

def renderArtist(request):
    arts = artist.objects.all
    return render(request, "artist.html", {"arts": arts})

def artist_detail(request, art_username):
    arts = artist.objects.get(username=art_username)
    posts = post.objects.order_by("-date").filter(author=art_username)
    bookings = booking.objects.order_by("date").filter(artist=art_username, date__gte=date.today())
    return render(request, "artist_detail.html", {"art": arts, "posts": posts, "books":bookings})