""" System Module """
from django.contrib import admin
from .models import Order, OrderBox, Address, Payment


class OrderBoxAdmin(admin.ModelAdmin):
    list_display = [
        'box',
        'order_box',
        'quantity',
        'date_added'
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'date_ordered',
        'ordered',
        'billing_address',
        'shipping_address',
        'payment'
    ]


class AddressAdmin(admin.ModelAdmin):
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
