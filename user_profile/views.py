from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Order, OrderBox, Address
from .forms import UserShippingAddressForm,UserBillingAddressForm
from .models import UserProfile



def profile(request):
    customer = get_object_or_404(UserProfile, customer=request.user)

    if request.method == 'GET':
        def get_customer_address(customer,address_type):
            address_qs = Address.objects.filter(
                customer=customer.customer,
                address_type=address_type,
                default=True
                )
            if address_qs.exists():
                address_qs = address_qs.last()
                print(address_qs.__dict__)
                user_address=address_qs
                print("address exists")
            return user_address
            
        cust_shipping_address = get_customer_address(customer,'S')
        cust_billing_address = get_customer_address(customer,'B')

    if request.method == 'POST':
        form = UserBillingAddressForm(request.POST, profile)

        if form.is_valid():
            # form.save()
            print(form.__dict__)
            default_address=Address(
                            customer=customer.customer,
                            address1=form.cleaned_data.get('default_address1'),
                            address2=form.cleaned_data.get('default_address2'),
                            county=form.cleaned_data.get('default_county'),
                            country=form.cleaned_data.get('default_country'),
                            eircode=form.cleaned_data.get('default_eircode'),
                            address_type='B',
                            default= True
                        )
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
                default_address.save()
                messages.success(request, 'Profile was updated.')
            else:
                messages.success(request, 'Profile address unchanged.')

        else:
            messages.error(request, ' Form invalid')
    
    shippingAddressForm = UserShippingAddressForm(instance=cust_shipping_address)
    billingAddressForm = UserBillingAddressForm(instance=cust_billing_address)
    ordered_boxes = customer.ordered_boxes.all()
    template = 'user_profile/profiles.html'
    context = {
        'shippingAddressForm': shippingAddressForm,
        'billingAddressForm': billingAddressForm,
        'ordered_boxes': ordered_boxes,
    }
    return render(request, template, context)

