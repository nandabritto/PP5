""" System Module """
from django.shortcuts import render
from .models import Order


def order(request):
    """
    A view to return order page
    """
    return render(request, 'order/order.html')


def checkout(request):
    """
    A view to return checkout page
    """
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderbox_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': True}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}

    return render(request, 'order/checkout.html')