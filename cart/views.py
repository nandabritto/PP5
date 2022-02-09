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
        cart_items = order.get_cart_items
        request.session['cart_items'] = cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = order['get_cart_items']

    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'cart/cart.html', context)


def update_cart(request):
    """
    A view to update cart items
    """
    data = json.loads(request.body)
    box_id = data['box_id']
    action = data['action']
    # 
    prod_selected_ids = data['prod_selected_ids']
    # box_prod2 = data['boxprod']
    print(f'selected product list: {prod_selected_ids}')
    # print(f'selected product list: {box_prod2}')
    customer = request.user
    box = Box.objects.get(id=box_id)
    order, created = Order.objects.get_or_create(
            customer=customer, ordered=False)

    order_box, created = OrderBox.objects.get_or_create(
        order_box=order, box=box)

    if action == 'add':
        order_box.quantity = (order_box.quantity + 1)
    elif action == 'remove':
        order_box.quantity = (order_box.quantity - 1)

    order_box.save()

    if order_box.quantity <= 0:
        order_box.delete()

    return JsonResponse('Item was added', safe=False)


def cart_number_on_all_pages(request):
    """
    Add cart items number in all pages
    """
    customer = request.user
    order = Order.objects.filter(
        customer=customer, ordered=False)
    cart_items = order.get_cart_items
    return {'cart_items': cart_items}
