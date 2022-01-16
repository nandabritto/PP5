""" System Module """
from django.shortcuts import render
from order.models import Order, OrderBox
from products.models import Box
from django.http import JsonResponse
import json


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

def updateCart(request):
    data = json.loads(request.body)
    boxId = data['boxId']
    action = data['action']


    customer = request.user
    box = Box.objects.get(id=boxId)
    order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

    orderBox, created = OrderBox.objects.get_or_create(order_box=order, box=box)

    if action == 'add':
        orderBox.quantity = (orderBox.quantity + 1 )
    elif action == 'remove':
        orderBox.quantity = (orderBox.quantity - 1)

    orderBox.save()

    if orderBox.quantity <= 0:
        orderBox.delete()

    return JsonResponse('Item was added', safe=False)