""" System Module """
from django.db import models


class Product(models.Model):
    """
    Create products to be added on boxes
    """
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    product_description = models.TextField()
    product_image = models.ImageField(null=True)

    def __str__(self):
        """ Return product name string """
        return str(self.product_name).lower()


class Box(models.Model):
    """
    Create reginal boxes
    """
    box_name = models.CharField(max_length=200)
    box_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    category = models.CharField(max_length=50, unique=True)
    box_description = models.TextField()
    box_image = models.ImageField(null=True)

    def __str__(self):
        """ Return box name string """
        return str(self.box_name).lower()


class Product_On_Box(models.Model):
    """
    Link products to their boxes
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    box = models.ForeignKey(
        Box, on_delete=models.CASCADE)
    product_selectable = models.BooleanField()

    def __str__(self):
        """ Return product name string """
        return f"{self.box.box_name} | {self.product.product_name}"