from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Blog, Category
from django.db.models import Q


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    # category = get_object_or_404(Category, pk=category_id)
    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)


def test(request):
    return render(request, 'test.html')

def blogs(request, slug):
    single_blog_post = get_object_or_404(Blog, status='Published', slug=slug)
    context = {
        'single_blog_post': single_blog_post,
    }
    return render(request, 'blogs.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    # blog = Blog.objects.filter(title__icontains=keyword, status='Published')
    blog = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status='Published')
    context = {
        'blog': blog,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)

