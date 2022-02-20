""" System Module """
from django.contrib import admin
from .models import Product, Box, ProductOnBox


admin.site.register(Product)
admin.site.register(Box)
admin.site.register(ProductOnBox)