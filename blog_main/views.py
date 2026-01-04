from django.shortcuts import render
from blogs.models import Blog, AboutUs, SocialMedia # Category [Check context processors]


def home(request):    
    featured_posts = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    un_featured_posts = Blog.objects.filter(is_featured=False)
    
    about_us_section = AboutUs.objects.all()

    context = {
        'featured_posts': featured_posts,
        'un_featured_posts': un_featured_posts,
        'about_us_section': about_us_section,
    }
    return render(request, 'homepage.html', context)
