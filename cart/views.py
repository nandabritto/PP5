""" System Module """
from django.shortcuts import render
from order.models import Order
from django.http import JsonResponse


def cart(request):
    """
    A view to return cart page
    """
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderbox_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order,}

    return render(request, 'cart/cart.html', context)


def updateBox(request):
    pass
