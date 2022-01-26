""" System Module """
import json
from django.shortcuts import render
from django.http import JsonResponse
from order.models import Order, OrderBox
from products.models import Box


def cart(request):
    """
    A view to return cart page
    """
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, ordered=False)
        items = order.orderbox_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}

    return render(request, 'cart/cart.html', context)


def updateCart(request):
    """
    A view to update cart items
    """
    data = json.loads(request.body)
    boxId = data['boxId']
    action = data['action']

    customer = request.user
    box = Box.objects.get(id=boxId)
    order, created = Order.objects.get_or_create(
            customer=customer, ordered=False)

    orderBox, created = OrderBox.objects.get_or_create(
        order_box=order, box=box)

    if action == 'add':
        orderBox.quantity = (orderBox.quantity + 1)
    elif action == 'remove':
        orderBox.quantity = (orderBox.quantity - 1)

    orderBox.save()

    if orderBox.quantity <= 0:
        orderBox.delete()

    return JsonResponse('Item was added', safe=False)
