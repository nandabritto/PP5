""" System Module """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Box
from .forms import ProductChoicesForm, BoxForm


def boxes(request):
    """
    Get objects from box modeland render boxes view
    """
    boxes = Box.objects.all()
    return render(request, 'products/products.html', {'boxes': boxes})


def product_detail(request, pk):
    """
    Get and filter objects from Box model and render box detail view
    """
    box = get_object_or_404(Box, pk=pk)
    context = {
        'box': box,
    }
    context['form'] = ProductChoicesForm(pk)
    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """
    Add product to the store
    """
    if request.method == 'POST':
        form = BoxForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your product was added')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Error adding your product. Please ensure your form is valid')
    
    else:
        form = BoxForm

    context = {
        'form': form,
    }
    return render(request, 'products/add_products.html', context)
