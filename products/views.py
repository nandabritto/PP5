""" System Module """
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Box
from .forms import ProductChoicesForm, BoxForm
from django.contrib.auth.decorators import login_required


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


@login_required
def add_product(request):
    """
    Add product to the store
    """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BoxForm(request.POST, request.FILES)
            if form.is_valid():
                box = form.save()
                messages.success(request, 'Your product was added')
                return redirect(reverse('product_details', args=[box.id]))
            else:
                messages.error(request, 'Error adding your product. Please, ensure your form is valid')
        
        else:
            form = BoxForm

        context = {
            'form': form,
        }
        return render(request, 'products/add_products.html', context)

    else:
        messages.error(request, 'Sorry, you do not have permittion to access this page')
        return render(request, 'home/index1.html')


@login_required
def edit_product(request, pk):
    """
    Edit product on the store
    """
    if request.user.is_superuser:
        box = get_object_or_404(Box, pk=pk)
        if request.method == 'POST':
            form = BoxForm(request.POST, request.FILES, instance=box)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your product was edited')
                box = get_object_or_404(Box, pk=pk)
                context = {
                    'box': box,
                }
                return render(request, 'products/product_detail.html', context)

             
            else:
                messages.error(request, 'Failed to edit your product. Please, ensure your form is valid')

        else:
            form = BoxForm(instance=box)
            messages.info(request, f'You are editing Box {box.box_name}')

        context = {
            'form': form,
            'box': box,
        }
        return render(request, 'products/edit_products.html', context)
    else:
        messages.error(request, 'Sorry, you do not have permittion to access this page')
        return render(request, 'home/index1.html')


@login_required
def delete_product(request, pk):
    """
    Delete product on the store
    """
    if request.user.is_superuser:
        box = get_object_or_404(Box, pk=pk)
        box.delete()
        messages.success(request, 'Product was deleted')
        return redirect(reverse('boxes'))
    else:
        messages.error(request, 'Something went wrong. Your product was not deleted.')