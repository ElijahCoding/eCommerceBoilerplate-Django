from django.shortcuts import render

def cart_home(request):
    return render(request, 'carts/home.html', {})

def cart_update(request):
    pass