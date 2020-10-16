from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect  # 能够立即去post_detail页面创建新的博客内容


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # 使用form.save保存表单,commit=False意味着我们还不想保存Post模型—我们想首先添加作者,大多数情况下，当你使用form.save()时，不会使用commit=False，但是在这种情况下，我们需要这样做。
            post.author = request.user  # 添加一个作者（因为 PostForm 中没有author字段，然而这个字段是必须的！）
            post.published_date = timezone.now()
            post.save()  # post.save()会保留更改（添加作者），并创建新的博客文章！
            return redirect('post_detail', pk=post.pk)  # 创建完新帖子我们就转去post_detail页面
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
