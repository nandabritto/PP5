from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import UserForm

def products(request):
    boxes = Product.objects.all()

    return render(request, 'products/products.html', {'boxes':boxes})

def product_detail(request, pk):
    context = {

    }
    context['form']= UserForm()
    return render(request, 'products/product_detail.html', context)