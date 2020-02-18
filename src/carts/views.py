from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    return render(request, 'carts/home.html', { "cart": cart_obj })

def cart_update(request):
    pass