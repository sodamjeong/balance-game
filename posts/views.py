from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('posts:index')
            
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comments = post.comment_set.all()
    comment_form = CommentForm()
    context = {
        'comments': comments,
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def answer(request, post_pk, answer):
    post = Post.objects.get(pk=post_pk)

    if answer == post.select1_content:
        post.select1_users.add(request.user)
    elif answer == post.select2_content:
        post.select2_users.add(request.user)

    return redirect('posts:detail', post.pk)



def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:detail', post.pk)

@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        form.save()
        return redirect('posts:detail', post_pk)
    detail(request, post_pk)