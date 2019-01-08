from django.urls import path
from .views import HomePageView, ShopView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
]
