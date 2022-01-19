""" System Module """
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CheckoutForm
from .models import Order, BillingAddress, OrderBox
from django.core.exceptions import ObjectDoesNotExist


def order(request):
    """
    A view to return order page
    """
    return render(request, 'order/order.html')


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)
            items = order.orderbox_set.all()
            cartItems = order.get_cart_items
            context = {
                'form': form,
                'items': items, 
                'order': order, 
                'cartItems': cartItems
            }
            return render(self.request, 'order/checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(customer=self.request.user, complete=False)
            if form.is_valid():
                address1 = form.cleaned_data.get('address1')
                address2 = form.cleaned_data.get('address2')
                county = form.cleaned_data.get('county')
                country = form.cleaned_data.get('country')
                eircode = form.cleaned_data.get('eircode')
                # same_shipping_address = form.cleaned_data.get('same_shipping_address')
                # save_info = form.cleaned_data.get('save_info')
                billing_address = BillingAddress(
                    customer = self.request.user,
                    address1 = address1,
                    address2 = address2,
                    county = county,
                    country = country,
                    eircode = eircode                
                )
                print(billing_address)
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                return redirect('checkout')
            messages.warning(self.request, "Failed checkout")
            return redirect("cart")
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order" )
            return redirect("cart")


class PaymentView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'order/payment.html')