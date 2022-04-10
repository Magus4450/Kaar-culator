

from turtle import st
from typing import Any
from xmlrpc.client import FastParser
from django.shortcuts import render, get_object_or_404
from .models import NewsModel, Category
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .forms import PostForm, UpdateForm

class NewsListView(ListView):
    model = NewsModel
    template_name = 'templates/news/news.html'
    context_object_name = 'news_list'

    def get_context_data(self, *args, **kwargs):

        cat_list = Category.objects.all()
        context = super(NewsListView, self).get_context_data(*args, **kwargs)
        context["cat_list"] = cat_list
        
        return context


def CategoryView(request, cats):
    category_posts = NewsModel.objects.filter(category=cats.replace("-", ""))
    cat_list = Category.objects.all()
    return render(request, 'templates/news/categories.html', {'cats': cats.title().replace("-", " "), 'category_posts': category_posts, 'cat_list': cat_list})

class NewsDetailView(DetailView):
    context_object_name = 'news'
    model = NewsModel
    template_name = 'templates/news/news_detail.html'

    def get_context_data(self, *args, **kwargs):



        context = super(NewsDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(NewsModel, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

    

class AddNewsView(CreateView):
    model = NewsModel
    form_class = PostForm
    template_name = 'templates/news/add_news.html'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'templates/news/add_category.html'
    fields = '__all__'

    
    

class UpdateNewsView(UpdateView):
    model = NewsModel
    form_class = UpdateForm
    template_name = 'templates/news/update_news.html'
    context_object_name = 'news'


class DeleteNewsView(DeleteView):
    context_object_name = 'news'
    model = NewsModel
    template_name = 'templates/news/delete_news.html'
    success_url = reverse_lazy("news:list")

def LikeView(request, pk):
    post = get_object_or_404(NewsModel, id=request.POST.get('post_id'))

    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True


    return HttpResponseRedirect(reverse('news:detail', args=[str(pk)]))

    