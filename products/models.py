""" System Module """
from django.db import models
from django.db.models import UniqueConstraint
from PIL import Image


class Product(models.Model):
    """
    Create products to be added on boxes
    """
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    product_description = models.TextField()
    product_note1 = models.TextField(null=True, blank=True)
    product_note2 = models.TextField(null=True, blank=True)
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
    category = models.CharField(max_length=50)
    box_description = models.TextField()
    box_image = models.ImageField(null=True, blank=True)
    box_note1 = models.TextField(null=True, blank=True)
    box_note2 = models.TextField(null=True, blank=True)

    def __str__(self):
        """ Return box name string """
        return str(self.box_name).lower()

    # def save(self):
    #     super().save()

    #     img = Image.open(self.box_image)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.box_image)


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
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=['product', 'box'],
                name='productsunique',
            ),
        ]
