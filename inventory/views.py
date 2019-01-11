from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Product, Category
from django.urls import reverse_lazy


class AddProduct(CreateView):
    model = Product
    template_name = 'addproduct.html'
    fields = '__all__'


class AddCategory(CreateView):
    model = Category
    template_name = 'addcategory.html'
    fields = '__all__'


class RemoveProduct(DeleteView):
    model = Product
    template_name = 'removeproduct.html'
    success_url = reverse_lazy('inventory')


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'editproduct.html'
    fields = '__all__'


class Inventory(ListView):
    model = Product
    template_name = 'inventory.html'
    context_object_name = 'products'
