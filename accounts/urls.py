from django.urls import path, include
from .views import login_view, register_view, profile_view, logout_view
app_name='accounts'
from home.views import home_view


urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('profile/', home_view, name="profile"),
    path('logout/', logout_view, name="logout"),
]



 