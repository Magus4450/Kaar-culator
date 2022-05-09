from django.urls import path, include
from .views import login_view, register_view, logout_view, profile_view, deactivate_view, activate_view, user_csv
app_name='accounts'



urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile_view, name="account"),
    path('deactivate/<int:pk>/', deactivate_view, name="deactivate"),
    path('activate/<int:pk>/', activate_view, name="activate"),
    path('download-csv/', user_csv, name="user_csv"),
]



 