""" System Module """
from django.contrib import admin
from .models import Product, Box, Product_On_Box


admin.site.register(Product)
admin.site.register(Box)
admin.site.register(Product_On_Box)