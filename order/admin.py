""" System Module """
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Order, OrderBox, Address, Payment


class OrderBoxAdmin(admin.ModelAdmin):
    """
    Create Order box option on admin
    """
    def order_number(self, obj):
        """
        Add id number to order
        """
        url = reverse('admin:order_order_change', args=[obj.order_box])
        return format_html("<a href='{}'>{}</a>", url, obj.order_box)

    list_display = [
        'box',
        'order_box',
        'quantity',
        'date_added',
        # 'get_order_admin',
        'order_number'
    ]


class OrderAdmin(admin.ModelAdmin):
    """
    Create Order option on admin
    """
    list_display = [
        'customer',
        'date_ordered',
        'ordered',
        'billing_address',
        'shipping_address',
        'payment',
        'id'
    ]


class AddressAdmin(admin.ModelAdmin):
    """
    Create Address option on admin
    """
    list_display = [
        'customer',
        'address1',
        'address2',
        'county',
        'country',
        'eircode',
        'address_type',
        'default'
    ]

    list_filter = ['country', 'default', 'address_type']
    search_fields = ['customer', 'address1', 'eircode']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderBox, OrderBoxAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Payment)
