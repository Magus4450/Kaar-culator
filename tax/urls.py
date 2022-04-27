
from django.urls import path
from .views import tax_view, TaxDetailView
app_name = "tax"

urlpatterns = [
    path('', tax_view, name="tax"),
    path('detail/<int:pk>/', TaxDetailView.as_view(), name="detail"),

]



 