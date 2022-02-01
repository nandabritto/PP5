from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Order, OrderBox, Address
from .forms import UserProfileForm
from .models import UserProfile



def profile(request):
    profile = get_object_or_404(UserProfile, customer=request.user)

    if request.method == 'GET':
        default_address_qs = Address.objects.filter(
            customer=profile.customer,
            address_type='B',
            default=True
            )
        if default_address_qs.exists():
            default_address_qs = default_address_qs.last()
            print(default_address_qs.__dict__)
            profile.default_address1 = default_address_qs.address1
            profile.default_address2 = default_address_qs.address2
            profile.default_county = default_address_qs.county
            profile.default_country = default_address_qs.country
            profile.default_eircode = default_address_qs.eircode

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)

        if form.is_valid():
            # form.save()
            print(form.__dict__)
            default_address=Address(
                            customer=profile.customer,
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
    
    form = UserProfileForm(instance=profile)
    ordered_boxes = profile.ordered_boxes.all()
    template = 'user_profile/profiles.html'
    context = {
        'form': form,
        'ordered_boxes': ordered_boxes,
    }
    return render(request, template, context)

