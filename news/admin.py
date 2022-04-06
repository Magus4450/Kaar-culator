from django.contrib import admin
from .models import NewsModel, Category

admin.site.register(NewsModel)
admin.site.register(Category)
