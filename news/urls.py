from django.urls import path
from .views import NewsListView, NewsDetailView, AddNewsView, UpdateNewsView, DeleteNewsView, AddCategoryView, CategoryView, LikeView, pin_news, unpin_news
app_name='news'


urlpatterns = [
    path('', NewsListView.as_view(), name="list"),
    path('<int:pk>/', NewsDetailView.as_view(), name="detail"),
    path('add/', AddNewsView.as_view(), name="add"),
    path('addcat/', AddCategoryView.as_view(), name="add_category"),
    path('update/<int:pk>/', UpdateNewsView.as_view(), name="update"),
    path('delete/<int:pk>/', DeleteNewsView.as_view(), name="delete"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('pin/<int:pk>', pin_news, name='pin_post'),
    path('unpin/<int:pk>', unpin_news, name='unpin_post'),
    
]



 