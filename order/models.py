from django.db import models
from django.contrib.auth.models import User 
from products.models import Box


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transactional_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.customer)

    @property
    def get_cart_total(self):
        orderitems = self.orderbox_set.all
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderbox_set.all
        total = sum([item.quantity for item in orderitems])
        return total


class OrderBox(models.Model):
    box = models.ForeignKey(Box, on_delete=models.SET_NULL, blank=True, null=True)
    order_box = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.box.box_price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address1 = models.CharField(max_length=100, null=True)
    addres2 = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=30, null=True)
    eircode = models.CharField(max_length=7, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return str(self.address1)