from django.shortcuts import render, get_object_or_404
from .models import Blog, Post

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogging/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    posts = Post.objects.filter(blog=blog, status='published')
    return render(request, 'blogging/blog_detail.html', {'blog': blog, 'posts': posts})

def post_detail(request, blog_slug, post_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    post = get_object_or_404(Post, slug=post_slug, blog=blog)
    return render(request, 'blogging/post_detail.html', {'post': post})
