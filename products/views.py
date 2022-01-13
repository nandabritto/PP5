""" System Module """
from django.shortcuts import render, get_object_or_404
from .models import Box
from .forms import ProductChoicesForm


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
