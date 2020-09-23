from django.shortcuts import redirect, render

from .forms import PostCreateForm
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post/post_list.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:post_list')
    else:
        form = PostCreateForm()
        context = {'form': form}
    return render(request, 'post/post_create.html', context)
