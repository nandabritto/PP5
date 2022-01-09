from django.shortcuts import render
from .models import Product

def products(request):
    boxes = Product.objects.all()

    return render(request, 'products/products.html', {'boxes':boxes})