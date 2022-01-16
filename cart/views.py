from django.shortcuts import render
from django.http import JsonResponse
from order.models import * 
from django.contrib.auth.models import User 
import logging
def cart(request):
    """
    A view to return index page 
    """

    if request.user.is_authenticated:
        customer =  request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderbox_set.all()
    else:
        items = []

    context = {'items': items, 'order':order,}
    
    return render(request, 'cart/cart.html', context)