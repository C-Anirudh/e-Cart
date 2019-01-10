from django.urls import path
from .views import AddProduct

urlpatterns = [
    path('inventory/', AddProduct.as_view(), name='addproduct'),
]
