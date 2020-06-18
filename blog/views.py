from django.shortcuts import render
from .models import Post, Category, Profile, About


def search_post(request):
        if request.method == 'POST':
                search_keyword = request.POST['search-keyword']
                posts = Post.objects.filter(title__icontains=search_keyword)
                context = {'posts': posts}
                return render(request, 'blog/search_post.html', context)
        return render(request, 'blog/search_post.html')

        
def detail_post(request, post_id):
        post = Post.objects.get(id=post_id)
        profile_obj = Profile.objects.get(user=post.author)
        context = {'posts': post, 'profile': profile_obj}
        return render(request, 'blog/detail_post.html', context)
    

def category_post(request, ctg_name):
    category_obj = Category.objects.get(name=ctg_name)
    category_post = Post.objects.filter(category=category_obj)
    context = {'category_post': category_post}
    return render(request, 'blog/category_post.html', context)



