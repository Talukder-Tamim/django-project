from django.shortcuts import render
from blog.models import Post, About

def home(request):
    post = Post.objects.order_by('-date')
    context = {'posts': post}
    return render(request, 'home.html', context)

def about(request):
        about_site = About.objects.all()
        context = {'sites': about_site}
        return render(request, 'blog/about.html', context)