from django.shortcuts import get_object_or_404
from products.models import Box
from order.models import Order

def order_contents(request):
    order_ctxt = []
    if request.user.is_authenticated:
        orders = Order.objects.filter(
            customer=request.user, ordered=True)
        for order in orders:
            # order_ctxt.append(order.id)
            # order_ctxt[order.id].append('items') = order.orderbox_set.all()
            # order_ctxt[order.id].append('itemsCount') = order.get_cart_items
            # order_ctxt[order.id].append('get_cart_total') = order.get_cart_total
            # order_ctxt[order.id].append('shipping') = order.shipping()
            order_ctxt.append({
                'order_id': order.id,
                'items': order.orderbox_set.all(),
                'itemsCount': order.get_cart_items,
                'get_cart_total': order.get_cart_total,
                'shipping': order.shipping(),
            })
    
    context = {
                'order_ctxt': order_ctxt
            }
    print(f'Print context: {context}')
    
    return context