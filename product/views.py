from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    queryset                = Product.objects.all()
    template_name           = "product/product.html" #Default is product/product_list.html

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     # print(context) Run this to see everything that is being passed
    #     return context