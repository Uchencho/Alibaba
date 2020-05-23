from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    queryset                = Product.objects.all()
    template_name           = "product/product.html" #Default is product/product_list.html

    # def get_context_data(self, *args, **kwargs):
    #     # To See the context that is being passed to the front
    #     # i.e return render("/product.html", context), where context is a dictionary containig object_list
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     # print(context) Run this to see everything that is being passed
    #     return context


class ProductDetailView(DetailView):
    queryset                = Product.objects.all()
    template_name           = "product/detail.html" #Default is product/product_list.html