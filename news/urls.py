from django.urls import path
from .views import NewsListView, NewsDetailView, AddNewsView, UpdateNewsView, DeleteNewsView, AddCategoryView, CategoryView, LikeView
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
    
]



 