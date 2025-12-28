from django.shortcuts import render
from blogs.models import Blog, Category



def home(request):
    categories = Category.objects.all()
    
    featured_posts = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    un_featured_posts = Blog.objects.filter(is_featured=False)
    
    context = {
        "categories": categories,
        'featured_posts': featured_posts,
        'un_featured_posts': un_featured_posts,
    }
    return render(request, 'homepage.html', context)
