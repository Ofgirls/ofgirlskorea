from time import sleep

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm, CommentForm, PasswordCheckForm
from django.http import Http404, HttpResponse
from django.template import Context, loader


# Create your views here.
def post_list(request):
    posts = Post.objects.filter().order_by('-published_date')
    categories = Category.objects.filter().order_by('name')
    template_name = 'bamboo/post_list.html'
    context_data = {'posts': posts, 'categories': categories}
    return render(request, template_name, context_data)


def post_list_by_tag(request, pk):
    posts = Post.objects.filter(category=pk).order_by('-published_date')
    categories = Category.objects.filter().order_by('name')
    template_name = 'bamboo/post_list_by_tag.html'
    context_data = {'posts': posts, 'categories': categories}
    return render(request, template_name, context_data)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    template_name = 'bamboo/post_detail.html'
    context_data = {'post': post, }
    return render(request, template_name, context_data)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'bamboo/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'bamboo/post_edit.html', {'form': form})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'bamboo/add_comment_to_post.html', {'form': form})


def post_edit_check_password(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PasswordCheckForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == post.post_password:
                return redirect('post_edit', pk=post.pk)
            else:
                return redirect('password_check', pk=post.pk)
    else:
        form = PasswordCheckForm()
        return render(request, 'bamboo/post_password_check.html', {'form': form})

"""
def bamboo_home(request):
    return render(request, 'bamboo/bamboo_home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'bamboo/bamboo_signup.html', {'form': form})
"""
