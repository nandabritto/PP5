
def cart_contents(request):
    """
    Creates cart items context
    """
    cart_items = request.session.get('cart_items', {}) 
    context = {
                'cart_items': cart_items
            }
    return context

