""" System Module """
from django.shortcuts import render


def order(request):
    """
    A view to return order page
    """
    return render(request, 'order/order.html')
