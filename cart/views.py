""" System Module """
import json
from django.shortcuts import render
from django.http import JsonResponse
from order.models import Order, OrderBox
from products.models import Box, Product


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

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        }
    return render(request, 'cart/cart.html', context)


def update_cart(request):
    """
    A view to update cart items
    """
    data = json.loads(request.body)
    box_id = data['box_id']
    action = data['action']

    customer = request.user

    # Get user selected products
    prod_selected_ids = data.get('prod_selected_ids', [])
    prod_selected = Product.objects.filter(
        id__in=[int(prd) for prd in prod_selected_ids])
    prod_selected_names = ', '.join([
        prd.product_name for prd in prod_selected])

    surprise_products = 'Surprise products will be added to your box.'

    # creates a box
    box = Box.objects.get(id=box_id)
    order, created = Order.objects.get_or_create(
            customer=customer, ordered=False)

    order_box, created = OrderBox.objects.get_or_create(
        order_box=order, box=box)

    if created:
        order_box.selected_products = prod_selected_names

    if action == 'add':
        order_box.quantity = (order_box.quantity + 1)
        if prod_selected_names.__len__() > 0:
            order_box.selected_products = prod_selected_names
        else:
            order_box.selected_products = surprise_products
    elif action == 'remove':
        order_box.quantity = (order_box.quantity - 1)
    order_box.save()

    if order_box.quantity <= 0:
        order_box.delete()

    return JsonResponse('Item was added.', safe=False)
