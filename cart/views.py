from django.shortcuts import render


def cart(request):
    """
    A view to return index page 
    """
    return render(request, 'cart/cart.html')