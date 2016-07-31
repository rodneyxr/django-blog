from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, 'Successfully created')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post_create.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'title': post.title,
        'post': post
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        'title': "List",
        'post_list': queryset
    }
    return render(request, 'post_list.html', context)

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, 'Successfully updated')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post_update.html', context)

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, 'Post sucessfully deleted')
    return redirect('posts:list')
