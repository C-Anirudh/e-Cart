from django.db import models
from django.urls import reverse


class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName


class Product(models.Model):
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField(null=False)
    productBrand = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('shop')
