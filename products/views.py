from django.shortcuts import render, get_object_or_404
from .models import Product, Box, Product_On_Box
from .forms import ProductChoicesForm

def boxes(request):
    boxes = Box.objects.all()
    

    return render(request, 'products/products.html', {'boxes':boxes})

def product_detail(request, pk):

    box = get_object_or_404(Box, pk=pk)
    context = {
        'box': box,
    }
    context['form']= ProductChoicesForm(pk)
    
    
    return render(request, 'products/product_detail.html', context)