from django.views.generic import TemplateView


class ShopView(TemplateView):
    template_name = 'shop.html'


class HomePageView(TemplateView):
    template_name = 'home.html'
