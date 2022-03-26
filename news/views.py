

from django.shortcuts import render
from .models import NewsModel, Category
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
    return render(request, 'templates/news/categories.html', {'cats': cats.title().replace("-", " "), 'category_posts': category_posts})

class NewsDetailView(DetailView):
    context_object_name = 'news'
    model = NewsModel
    template_name = 'templates/news/news_detail.html'

    

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

class DeleteNewsView(DeleteView):
    context_object_name = 'news'
    model = NewsModel
    template_name = 'templates/news/delete_news.html'
    success_url = reverse_lazy("news:list")
    