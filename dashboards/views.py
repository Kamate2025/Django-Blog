from django.shortcuts import get_object_or_404, render, redirect
from blog_main.forms import RegistrationForm
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import AddUser, BlogForm, CategoryForm
from django.utils.text import slugify
from django.contrib.auth.models import User


@login_required(login_url='login')
def dashboard(request):
    total_categories = Category.objects.all().count()
    total_blogs = Blog.objects.all().count()
    context = {
        'total_categories': total_categories,
        'total_blogs': total_blogs,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories') 
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    context = {
        'category': category,
        'form': form,    } 
    return render(request, 'dashboard/edit_category.html', context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def cat_add_cancel(request):
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
        }
    return render(request, 'dashboard/posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) #save form data temporarily
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form = BlogForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')

def edit_post(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog.slug = slugify(title) + '-' + str(blog.id)
            form.save()
            return redirect('posts')
    form = BlogForm(instance=blog)        
    context = {
        'form': form,
        'blog': blog,
    }
    return render(request, 'dashboard/edit_post.html', context)


def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'dashboard/users.html', context)


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')


def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = AddUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = AddUser(instance=user)
    context = {
        'form': form,
        'user': user,
        }
    return render(request, 'dashboard/edit_user.html', context)


def add_user(request):
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = AddUser()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_user.html', context)
