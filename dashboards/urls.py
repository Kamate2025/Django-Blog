from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #categories
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('categories/add/cancel/', views.cat_add_cancel, name='cat_add_cancel'),
    
    #posts
    path('posts/', views.posts, name='posts'),
    path('posts/add/', views.add_post, name='add_post'),
]
