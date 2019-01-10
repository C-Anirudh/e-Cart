from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ShopView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'shop.html'


class HomePageView(TemplateView):
    template_name = 'home.html'
