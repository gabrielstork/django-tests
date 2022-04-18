from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from .models import Post
from .forms import PostForm, CommentForm


def index(request):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=request.POST.get('post'))

        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect('index')

    if request.user.is_authenticated:
        posts = Post.objects.filter(author__in=request.user.following.all())
        return render(request, 'posts/index.html', {'posts': posts})

    return render(request, 'posts/index.html')


@login_required
def discover(request):
    if request.method == 'POST':
        account = get_object_or_404(Account, id=request.POST.get('account'))

        if account in request.user.following.all():
            request.user.following.remove(account)
            account.followers.remove(request.user)
        else:
            request.user.following.add(account)
            account.followers.add(request.user)

        return redirect('discover')

    accounts = Account.objects.exclude(id=request.user.id)
    return render(request, 'posts/discover.html', {'accounts': accounts})


@login_required
def comments(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        return redirect('post', id=id)

    form = CommentForm()
    return render(request, 'posts/post.html', {'post': post, 'form': form})


@login_required
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        return redirect('index')

    form = PostForm()
    return render(request, 'posts/new.html', {'form': form})
