from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewBlogForm
from .models import Blog
from comments.models import Comment
from comments.forms import NewCommentForm

@login_required(login_url='accounts:login_path')
def create(request):
    if request.method == 'POST':
        form = NewBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blogs:read_path', id_b=blog.id)
    else:
        form = NewBlogForm()
    return render(request, 'blogs/create.html', { 'form': form })

def index(request):
    blogs = Blog.objects.all().order_by('created_on')
    return render(request, 'blogs/index.html', {
        'blogs': blogs,
    })

@login_required(login_url='accounts:login_path')
def read(request, id_b):
    blog = Blog.objects.get(id=id_b)
    comments = Comment.objects.filter(blog=blog).order_by('created_on').reverse()
    form = NewCommentForm()
    return render(request, 'blogs/read.html', {
        'blog': blog,
        'comments': comments,
        'form': form,
    })

@login_required(login_url='accounts:login_path')
def update(request, id_b):
    blog = Blog.objects.get(id=id_b)
    if request.user != blog.author:
        raise PermissionError
    if request.method == 'POST':
        form = NewBlogForm(request.POST, request.FILES)
        if form.is_valid():
            upt_blog = form.save(commit=False)
            blog.title = upt_blog.title
            blog.body = upt_blog.body
            blog.thumb = upt_blog.thumb
            blog.save()
            return redirect('blogs:read_path', id_b=id_b)
    else:
        form = NewBlogForm(instance=blog)
    return render(request, 'blogs/update.html', { 'form': form, 'blog': blog })


@login_required(login_url='accounts:login_path')
def delete(request, id_b):
    blog = Blog.objects.get(id=id_b)
    user = request.user
    if blog.author == user:
        blog.delete()
        return redirect('blogs:index_path')
    else:
        raise PermissionError

@login_required(login_url='accounts:login_path')
def upvote(request, id_b):
    user = request.user
    blog = Blog.objects.get(id=id_b)
    if blog not in user.likes.all():
        if blog in user.dislikes.all():
            user.dislikes.remove(blog)
            blog.downvotes = blog.downvotes - 1
        user.likes.add(blog)
        blog.upvotes = blog.upvotes + 1
    else:
        user.likes.remove(blog)
        blog.upvotes = blog.upvotes - 1
    blog.save()
    return redirect('blogs:read_path', id_b=id_b)

@login_required(login_url='accounts:login_path')
def downvote(request, id_b):
    user = request.user
    blog = Blog.objects.get(id=id_b)
    if blog not in user.dislikes.all():
        if blog in user.likes.all():
            user.likes.remove(blog)
            blog.upvotes = blog.upvotes - 1
        user.dislikes.add(blog)
        blog.downvotes = blog.downvotes + 1
    else:
        user.dislikes.remove(blog)
        blog.downvotes = blog.downvotes - 1
    blog.save()
    return redirect('blogs:read_path', id_b=id_b)