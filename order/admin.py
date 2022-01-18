from django.contrib import admin
from .models import Order, OrderBox, BillingAddress

admin.site.register(Order)
admin.site.register(OrderBox)
admin.site.register(BillingAddress)
