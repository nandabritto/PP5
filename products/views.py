from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import UserForm

def products(request):
    boxes = Product.objects.all()

    return render(request, 'products/products.html', {'boxes':boxes})

def product_detail(request, pk):

    box = get_object_or_404(Product, pk=pk)
    context = {
        'box': box,
    }
    
    return render(request, 'products/product_detail.html', context)