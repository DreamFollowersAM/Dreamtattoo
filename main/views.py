from django.shortcuts import render
from post.models import post

def renderHome(request):
    total_posts = post.objects.count()
    posts = post.objects.order_by("-date")
    return render(request, "home.html", {"posts": posts, "total_posts": total_posts})

def renderAbout(request):
    return render(request, "about.html")

def renderCares(request):
    return render(request, "cares.html")