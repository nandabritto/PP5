""" System Module """
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Order, OrderBox, Address
from .forms import UserAddressForm
from .models import UserProfile
from django.contrib.auth.models import User


@login_required()
def profile(request):
    """
    A view to return profile page 
    """
    return render(request, 'user_profile/profiles.html')


@login_required()
def update_profile(request):
    """
    Get customer, shipping and billing address and update
    """
    customer = get_object_or_404(UserProfile, customer=request.user)
    cust_shipping_address = Address()
    cust_billing_address = Address()

    if request.method == 'GET':
        def get_customer_address(customer, address_type):
            user_address = Address()
            address_qs = Address.objects.filter(
                customer=customer.customer,
                address_type=address_type,
                default=True
                )
            if address_qs.exists():
                address_qs = address_qs.last()
                print(address_qs.__dict__)
                user_address = address_qs
                print("address exists")
            return user_address

        cust_shipping_address = get_customer_address(customer, 'S')
        cust_billing_address = get_customer_address(customer, 'B')

    if request.method == 'POST':
        form = UserAddressForm(request.POST, instance=Address())
        print(request.POST.__dict__)
        if form.is_valid():
            default_address=Address(
                            customer=customer.customer,
                            address1=form.cleaned_data.get('address1'),
                            address2=form.cleaned_data.get('address2'),
                            county=form.cleaned_data.get('county'),
                            country=form.cleaned_data.get('country'),
                            eircode=form.cleaned_data.get('eircode'),
                            address_type=form.cleaned_data.get('address_type'),
                            default= True
                        )
            print('testeeee')
            print(default_address.__dict__)
            default_address_qs = Address.objects.filter(
                customer=default_address.customer,
                address1=default_address.address1,
                address2=default_address.address2,
                county=default_address.county,
                country=default_address.country,
                eircode=default_address.eircode,
                address_type=default_address.address_type,
            )
            if not default_address_qs.exists():
                address_qs = Address.objects.filter(
                    customer=default_address.customer,
                    address_type=default_address.address_type,
                    default=True)

                address_qs.update(default=False)

                default_address.save()
                messages.success(request, 'Profile was updated.')
            else:
                messages.success(request, 'Profile address unchanged.')
             
        else:
            messages.error(request, ' Form invalid')

    shipping_address_form = UserAddressForm(instance=cust_shipping_address)
    billing_address_form = UserAddressForm(instance=cust_billing_address)
    customer = request.user
    # ordered_boxes = order.ordered_boxes  

    template = 'user_profile/update_profile.html'
    context = {
        'shipping_address_form': shipping_address_form,
        'billing_address_form': billing_address_form,
        'customer': customer,
        # 'ordered_boxes': ordered_boxes,
    }
    return render(request, template, context)
