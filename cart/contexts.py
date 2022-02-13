from order.models import Order
# def cart_contents(request):
#     """
#     Creates cart items context
#     """
#     cart_items = request.session.get('cart_items', {})
#     context = {
#                 'cart_items': cart_items
#             }
#     return context


def cart_contents(request):
    """
    Creates order contexts to be callable in profile pages
    """
    cart_ctxt = []
    if request.user.is_authenticated:
        order = Order.objects.filter(
            customer=request.user, ordered=False)
        open_order = order[0]
    context = {
                'cartItemsCount': open_order.get_cart_items
            }
    return context