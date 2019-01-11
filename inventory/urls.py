from django.urls import path
from django.contrib.auth.decorators import permission_required
from .views import AddProduct, AddCategory, RemoveProduct, UpdateProduct, Inventory
urlpatterns = [
    path('inventory/', permission_required('is_staff')
         (Inventory.as_view()), name='inventory'),
    path('inventory/addproduct/', permission_required('is_staff')
         (AddProduct.as_view()), name='addproduct'),
    path('inventory/addcategory/', permission_required('is_staff')
         (AddCategory.as_view()), name='addcategory'),
    path('inventory/removeproduct//<int:pk>/', permission_required('is_staff')
         (RemoveProduct.as_view()), name='removeproduct'),
    path('inventory/<int:pk>/edit', permission_required('is_staff')
         (UpdateProduct.as_view()), name='editproduct'),
]
