from django.shortcuts import render
from django.http import JsonResponse


def cart(request):
    """
    A view to return index page 
    """
    return render(request, 'cart/cart.html')