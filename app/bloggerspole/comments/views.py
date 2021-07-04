from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import NewCommentForm
from blogs.models import Blog
from .models import Comment

@login_required(login_url='accounts:login_path')
def create(request, id_b):
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog = Blog.objects.get(id=id_b)
            comment.save()
    return redirect('blogs:read_path', id_b=id_b)
    
@login_required(login_url='accounts:login_path')
def delete(request, id_c):
    comment = Comment.objects.get(id=id_c)
    if request.user == comment.author:
        Comment.objects.get(id=id_c).delete()
        return redirect('blogs:read_path', id_b=comment.blog.id)
    else:
        raise PermissionError