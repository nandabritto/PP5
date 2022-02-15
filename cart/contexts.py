""" System Module """
from order.models import Order


def cart_contents(request):
    """
    Creates order contexts to be callable in profile pages
    """
    cart_items_count = 0
    if request.user.is_authenticated:
        order = Order.objects.filter(
            customer=request.user, ordered=False)
        if order.exists():
            open_order = order[0]
            cart_items_count = open_order.get_cart_items

    context = {
                'cart_items_count': cart_items_count
            }
    return context
