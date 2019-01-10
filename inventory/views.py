from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product


class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'inventory.html'
    fields = '__all__'
    login_url = 'login'
