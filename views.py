from django.shortcuts import render
from .models import Post


def blog_views(request):
    posts = list(Post.objects.all())
    context = {'posts': posts}
    return render(request, 'blog_page.html', context)
