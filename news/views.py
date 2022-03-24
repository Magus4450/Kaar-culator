from django.shortcuts import render
from .models import NewsModel
# ListView -> All news
# DetailView -> One news in detail
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = NewsModel
    template_name = 'templates/home.html'