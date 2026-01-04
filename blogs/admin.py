from django.contrib import admin
from .models import Category, Blog, AboutUs, SocialMedia


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
        }
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name')
    list_editable = ('is_featured', 'status',)
    
class AboutUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = AboutUs.objects.all().count()
        if count == 0:
            return True
        else:
            return False
    
    list_display = ('about_us_title', 'about_us_description', 'created_at')
    

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('social_media_name', 'link')

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)

