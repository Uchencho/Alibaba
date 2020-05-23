from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404

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
    #queryset                = Product.objects.all()
    template_name           = "product/detail.html" #Default is product/product_list.html

    def get_object(self, *args, **kwargs):
        # request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

class ProductFeaturedListView(ListView):
    # List all products that are featured
    template_name           = "product/featured-product.html" #Default is product/product_list.html
    queryset                = Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    # List all products that are featured
    template_name           = "product/featured-product-detail.html" #Default is product/product_list.html
    queryset                = Product.objects.featured()