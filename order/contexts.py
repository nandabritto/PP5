""" System Module """
from order.models import Order


def order_contents(request):
    """
    Creates order contexts to be callable in profile pages
    """
    order_ctxt = []
    if request.user.is_authenticated:
        orders = Order.objects.filter(
            customer=request.user, ordered=True).order_by('-date_ordered')
        for order in orders:
            items = order.orderbox_set.exclude(box__isnull=True)
            order_ctxt.append({
                'order_id': order.id,
                'items': items.all(),
                'itemsCount': order.get_cart_items,
                'get_cart_total': order.get_cart_total,
                'shipping': order.shipping(),
            })
    context = {
                'order_ctxt': order_ctxt
            }
    return context
