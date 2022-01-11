from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    category = models.ForeignKey(
        Box, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(null=True)

    def __str__(self):
        """ Return product name string """
        return str(self.product_name).lower()



