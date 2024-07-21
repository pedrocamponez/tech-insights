from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.http import JsonResponse
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/index.html', {'form': form, 'posts': Post.objects.all()})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
