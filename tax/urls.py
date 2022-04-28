
from django.urls import path
from .views import tax_view, TaxDetailView, tax_pdf
app_name = "tax"

urlpatterns = [
    path('', tax_view, name="tax"),
    path('detail/<int:pk>/', TaxDetailView.as_view(), name="detail"),
    path('detail_pdf/<int:pk>/', tax_pdf, name="detail_pdf"),

]



 