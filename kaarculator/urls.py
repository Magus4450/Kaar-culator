
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls', namespace='account')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls', namespace='home')),
    path('news/', include('news.urls', namespace='news')),
]
