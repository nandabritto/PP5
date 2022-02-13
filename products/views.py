""" System Module """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from product_review.forms import AddReviewForm
from product_review.models import BoxReview
from .models import Box, Product, Product_On_Box
from .forms import ProductChoicesForm, BoxForm, ProductForm, ProductOnBoxForm


def boxes(request):
    """
    Get objects from box modeland render boxes view
    """
    boxes = Box.objects.all()
    return render(request, 'products/products.html', {'boxes': boxes})


def box_detail(request, pk):
    """
    Get and filter objects from Box model and render box detail view
    """
    box = get_object_or_404(Box, pk=pk)

    if request.method == "POST" and request.user.is_authenticated:
        review_rating = request.POST.get('review_rating', 5)
        review_text = request.POST.get('review_text', '')

        review = BoxReview.objects.create(
            box=box,
            customer=request.user,
            review_rating=review_rating,
            review_text=review_text
            )
        return redirect(reverse('box_details', args=[box.id]))

    review_form = AddReviewForm
    reviews = BoxReview.objects.filter(box=box.id).order_by('-date_added')[:2]

    product_on_box = Product_On_Box.objects.filter(box=box.id)

    context = {
        'box': box,
        'review_form': review_form,
        'reviews': reviews,
        'product_on_box':product_on_box,
    }
    context['form'] = ProductChoicesForm(pk)
    return render(request, 'products/box_detail.html', context)


def product_detail(request, pk):
    """
    Get and filter objects from Box model and render box detail view
    """
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_box(request):
    """
    Add box to the store
    """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BoxForm(request.POST, request.FILES)
            if form.is_valid():
                box = form.save()
                messages.success(request, 'Your box was added')
                return redirect(reverse('box_details', args=[box.id]))
            else:
                messages.error(request, 'Error adding your box.\
                    Please, ensure your form is valid')
        else:
            form = BoxForm

        context = {
            'form': form,
        }
        return render(request, 'products/add_box.html', context)

    else:
        messages.error(request, 'Sorry, you do not have permittion \
            to access this page')
        return render(request, 'home/index.html')


@login_required
def add_product(request):
    """
    Add product to the store
    """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request, 'Your product was added')
                return redirect(reverse('product_details', args=[product.id]))
            else:
                messages.error(request, 'Error adding your product.\
                    Please, ensure your form is valid')
        else:
            form = ProductForm

        context = {
            'form': form,
        }
        return render(request, 'products/add_product.html', context)

    else:
        messages.error(request, 'Sorry, you do not have permittion \
            to access this page')
        return render(request, 'home/index.html')


@login_required
def add_product_on_boxes(request):
    """
    Add product on boxes to the store
    """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductOnBoxForm(request.POST, request.FILES)
            if form.is_valid():
                product_on_box = form.save()
                messages.success(request, 'Your product was added on the box')
                # return redirect(reverse('box_details', args=[box.id]))
            else:
                messages.error(request, 'Error adding your product on box.\
                    Please, ensure your form is valid')
        else:
            form = ProductOnBoxForm

        context = {
            'form': form,
        }
        return render(request, 'products/add_product_on_box.html', context)

    else:
        messages.error(request, 'Sorry, you do not have permittion \
            to access this page')
        return render(request, 'home/index.html')


@login_required
def edit_box(request, pk):
    """
    Edit box on the store
    """
    if request.user.is_superuser:
        box = get_object_or_404(Box, pk=pk)
        if request.method == 'POST':
            form = BoxForm(request.POST, request.FILES, instance=box)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your box was edited')
                box = get_object_or_404(Box, pk=pk)
                context = {
                    'box': box,
                }
                return render(request, 'products/box_detail.html', context)
            else:
                messages.error(request, 'Failed to edit your box.\
                    Please, ensure your form is valid')
        else:
            form = BoxForm(instance=box)
            messages.info(request, f'You are editing Box {box.box_name}')

        context = {
            'form': form,
            'box': box,
        }
        return render(request, 'products/edit_boxes.html', context)
    else:
        messages.error(request, 'Sorry, you do not  have permition \
            to access this page')
        return render(request, 'home/index.html')


@login_required
def delete_box(request, pk):
    """
    Delete product on the store
    """
    if request.user.is_superuser:
        try:
            box = get_object_or_404(Box, pk=pk)
            box.delete()
            messages.success(request, 'Box was deleted')
            return redirect(reverse('boxes'))
        except:
            messages.error(request, 'Something went wrong.\
                Your box was not deleted.')
            return redirect(reverse('box_details', args=[pk]))
    else:
        messages.error(request, 'Sorry, you do not have permittion \
            to access this page')
        return render(request, 'home/index.html')


@login_required
def edit_product(request, pk):
    """
    Edit products on the store
    """
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your product was edited')
                product = get_object_or_404(Product, pk=pk)
                context = {
                    'product': product,
                }
                return render(request, 'products/product_detail.html', context)
            else:
                messages.error(request, 'Failed to edit your product.\
                    Please, ensure your form is valid')
        else:
            form = ProductForm(instance=product)
            messages.info(
                request,
                f'You are editing Product {product.product_name}')

        context = {
            'form': form,
            'product': product,
        }
        return render(request, 'products/edit_products.html', context)
    else:
        messages.error(request, 'Sorry, you do not have permition \
            to access this page')
        return render(request, 'home/index.html')


@login_required
def delete_product(request, pk):
    """
    Delete product on the store
    """
    if request.user.is_superuser:
        try:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
            messages.success(request, 'Product was deleted')
            return redirect(reverse('products_list'))
        except:
            messages.error(request, 'Something went wrong.\
                Your product was not deleted.')
            return redirect(reverse('box_details', args=[pk]))
    else:
        messages.error(request, 'Sorry, you do not have permittion \
            to access this page')
        return render(request, 'home/index.html')


@login_required
def delete_productonbox(request, pk):
    """
    Delete product on box on the store
    """
    if request.user.is_superuser:
        try:
            productonbox = get_object_or_404(Product_On_Box, pk=pk)
            productonbox.delete()
            messages.success(request, 'Product was deleted from box')
            return redirect(reverse('productsonbox_list'))
        except:
            messages.error(request, 'Something went wrong.\
                Your product was not deleted from the box.')
            # return redirect(reverse('box_details', args=[pk]))
    else:
        messages.error(request, 'Sorry, you do not have permittion \
            to access this page')
        return render(request, 'home/index.html')


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Create super user only class
    """
    def test_func(self):
        return self.request.user.is_superuser


class ListBoxes(SuperUserRequiredMixin, ListView):
    """
    Creates a list of all boxes to admin
    """
    model = Box
    template_name = 'products/boxes_list.html'
    paginate_by = 20
    ordering = ['id']


class ListProducts(SuperUserRequiredMixin, ListView):
    """
    Creates a list of all boxes to admin
    """
    model = Product
    template_name = 'products/products_list.html'
    paginate_by = 20
    ordering = ['id']


class ListProductsOnBox(SuperUserRequiredMixin, ListView):
    """
    Creates a list of all boxes to admin
    """
    model = Product_On_Box
    template_name = 'products/productsonbox_list.html'
    paginate_by = 20
    ordering = ['id']
