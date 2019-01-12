from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from inventory.models import Product


class ShopView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'


class HomePageView(TemplateView):
    template_name = 'home.html'
