from django.shortcuts import render, get_object_or_404
from .models import post

def renderPosts(request):
    total_posts = post.objects.count()
    posts = post.objects.order_by("-date")
    return render(request, "mainPost.html", {"posts": posts, "total_posts": total_posts})