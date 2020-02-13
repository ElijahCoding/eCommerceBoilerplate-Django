from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Product


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self):
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/featured-detail.html"

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404('Product doesnt exist')
    #     return instance

    def get_queryset(self):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)