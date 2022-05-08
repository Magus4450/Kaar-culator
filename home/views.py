from .forms import FeedbackForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from ..news.models import Category
# Create your views here.
from news.models import NewsModel, Category


def home_view(request):
    # cat_list = Category.objects.first(4)
    cat_list = Category.objects.all()

    news_list = NewsModel.objects.all()

    return render(request, 'templates/home.html', {'cat_list': cat_list, 'news_list': news_list[:4]})


def about_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/')
        else:
            print("INCLEANS")
    else:
        form = FeedbackForm()
    return render(request, 'templates/about.html', {'form': form})

# def CategoryView(request, cats):
#     category_posts = NewsModel.objects.filter(category=cats.replace("-", ""))
#     return render(request, 'templates/news/categories.html', {'cats': cats.title().replace("-", " "), 'category_posts': category_posts})

