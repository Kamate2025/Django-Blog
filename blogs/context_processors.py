from .models import Category, SocialMedia


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def social_media_links(request):
    social_media = SocialMedia.objects.all()
    return dict(social_media=social_media)


