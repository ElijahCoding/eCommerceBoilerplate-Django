from django.shortcuts import render
from .models import Cart

def cart_home(request):
    cart_id = request.session.get('cart_id', None)

    qs = Cart.objects.filter(id=cart_id)
    if qs.cocunt() == 1:
        cart_obj = qs.first()
    else:
        cart_obj = Cart.objects.create(user=None)
        request.session['cart_id'] = cart_obj.id

    return render(request, 'carts/home.html', {})

def cart_update(request):
    pass