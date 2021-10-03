from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'blog/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    form_class = UpdateForm
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')
