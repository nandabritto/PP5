""" System Module """
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from user_profile.models import Address
from user_profile.models import UserProfile
from .forms import CheckoutForm
from .models import Order, Payment
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def is_valid_form(values):
    """
    Validate form if fields are empty
    """
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class CheckoutView(View):
    """
    A view to return checkout page
    """
    def get(self, *args, **kwargs):
        """
        Get the checkout form and display in page
        """
        form = CheckoutForm()
        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(
                customer=customer, ordered=False)
            items = order.orderbox_set.all()
            cart_items = order.get_cart_items
            context = {
                'form': form,
                'items': items,
                'order': order,
                'cart_items': cart_items,
            }

            shipping_address_qs = Address.objects.filter(
                customer=customer,
                address_type='S',
                default=True
                )
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]}
                    )

            billing_address_qs = Address.objects.filter(
                customer=customer,
                address_type='B',
                default=True
                )
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]}
                    )

            return render(self.request, 'order/checkout.html', context)

    def post(self, *args, **kwargs):
        """
        Create an order and link to shipping address
        """
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(
                customer=self.request.user, ordered=False)
            if form.is_valid():

                # Create default shipping address
                use_default_shipping = form.cleaned_data.get(
                    'use_default_shipping')

                # if default shipping address checked
                if use_default_shipping:
                    # creates shipping address queryset
                    address_qs = Address.objects.filter(
                        customer=self.request.user,
                        address_type='S',
                        default=True
                    )
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shipping_address = shipping_address
                        order.save()
                    else:
                        messages.info(
                            self.request, 'No default shipping address')
                        return redirect('checkout')
                else:
                    shipping_address1 = form.cleaned_data.get(
                        'shipping_address1')
                    shipping_address2 = form.cleaned_data.get(
                        'shipping_address2')
                    shipping_county = form.cleaned_data.get(
                        'shipping_county')
                    shipping_country = form.cleaned_data.get(
                        'shipping_country')
                    shipping_eircode = form.cleaned_data.get(
                        'shipping_eircode')
                    # same_shipping_address = form.cleaned_data.get(
                    # 'same_shipping_address')
                    # save_info = form.cleaned_data.get('save_info')

                    if is_valid_form([
                        shipping_address1,
                        shipping_country,
                        shipping_eircode]):
                        shipping_address = Address(
                            customer=self.request.user,
                            address1=shipping_address1,
                            address2=shipping_address2,
                            county=shipping_county,
                            country=shipping_country,
                            eircode=shipping_eircode,
                            address_type='S'
                            )
                        shipping_address.save()
                        order.shipping_address = shipping_address
                        order.save()

                        set_default_shipping = form.cleaned_data.get(
                            'set_default_shipping')
                        if set_default_shipping:
                            shipping_address.default = True
                            shipping_address.save()
                    else:
                        messages.info(
                            self.request, "Please fill in the \
                            required shipping address fields")
                        return redirect('checkout')

                # Creates default billing address
                use_default_billing = form.cleaned_data.get(
                    'use_default_billing')
                same_billing_address = form.cleaned_data.get(
                    'same_billing_address')

                if same_billing_address:
                    billing_address = shipping_address
                    billing_address.pk = None
                    billing_address.save()
                    billing_address.address_type = 'B'
                    billing_address.save()
                    order.billing_address = billing_address
                    order.save()

                # if default billing address checked
                elif use_default_billing:
                    # creates billing address queryset
                    address_qs = Address.objects.filter(
                        customer=self.request.user,
                        address_type='B',
                        default=True
                    )
                    if address_qs.exists():
                        billing_address = address_qs[0]
                        order.billing_address = billing_address
                        order.save()
                    else:
                        messages.info(
                            self.request, 'No default billing address')
                        return redirect('checkout')
                else:
                    billing_address1 = form.cleaned_data.get(
                        'billing_address1')
                    billing_address2 = form.cleaned_data.get(
                        'billing_address2')
                    billing_county = form.cleaned_data.get(
                        'billing_county')
                    billing_country = form.cleaned_data.get(
                        'billing_country')
                    billing_eircode = form.cleaned_data.get(
                        'billing_eircode')

                    if is_valid_form([
                        billing_address1,
                        billing_country,
                        billing_eircode]):
                        billing_address = Address(
                            customer=self.request.user,
                            address1=billing_address1,
                            address2=billing_address2,
                            county=billing_county,
                            country=billing_country,
                            eircode=billing_eircode,
                            address_type='B'
                        )
                        billing_address.save()
                        # Set billing address to order
                        order.billing_address = billing_address
                        order.save()
                        # Set default billing address
                        set_default_billing = form.cleaned_data.get(
                            'set_default_billing')
                        if set_default_billing:
                            billing_address.default = True
                            billing_address.save()
                    else:
                        messages.info(
                            self.request, "Please fill in the \
                                required billing address fields")
                        return redirect('checkout')

                return redirect('checkout_summary')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("cart")


def checkout_summary(request):
    order = Order.objects.get(
        customer= request.user, ordered=False)
    items = order.orderbox_set.all()
    cart_items = order.get_cart_items
    shipping = order.shipping()

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        'shipping':shipping,
    }
    return render(request, "order/checkout_summary.html",context )


class PaymentView(View):
    """
    Create a payment view
    """
    def get(self, *args, **kwargs):
        """
        Get the payment url
        """
        return render(self.request, "order/payment.html")

    def post(self, *args, **kwargs):
        """
        Post form with order details and payment
        """
        order = Order.objects.get(
            customer=self.request.user, ordered=False)
        token = self.request.POST.get('stripeToken')
        amount = int(order.get_cart_total * 100)

        try:
            # create charge in euro
            charge = stripe.Charge.create(
                amount=amount,
                currency="eur",
                source=token,
            )
            # create stripe payment and save
            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.customer = self.request.user
            payment.amount = order.get_cart_total
            payment.save()
            # create and save order
            order.ordered = True
            order.payment = payment
            order.save()
            messages.success(
                self.request, "Your order was successful")
            return redirect("success", order.pk)

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            messages.error(self.request, f"{err.get('message')}")
            return redirect("/")

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.error(self.request, "Rate Limited Error")
            return redirect("/")

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            messages.error(self.request, "Invalid parameter")
            return redirect("/")

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            messages.error(self.request, "Not authenticated")
            return redirect("/")

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.error(self.request, "Network error")
            return redirect("/")

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.error(self.request, "Something went wrong, \
                you were not charged. Try again.")
            return redirect("/")

        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            messages.error(self.request, "A serious error occurred.")
            return redirect("/")


@login_required
def success(request, pk):
    """
    Render a success page and send a purchase confirmation email
    """
    order = Order.objects.get(pk=pk)

    # if request.user.is_authenticated:
    #     profile = UserProfile.objects.get(customer=request.user)
    #     order.user_profile = profile
    #     order.save()

    #     if save_info:
    #         profile_data = {
    #             'default_address1': order.shipping_address.address1,
    #             'default_address2': order.shipping_address.address2,
    #             'default_county': order.shipping_address.county,
    #             'default_country': order.shipping_address.country,
    #             'default_eircode': order.shipping_address.eircode,
    #         }

    #         user_profile_form = UserProfileForm(profile_data, instance=profile)

    #         if user_profile_form.is_valid():
    #             user_profile_form.save()

    if order.customer == request.user:
        template = render_to_string(
            'order/email_template.html', {'name': request.user})
        email = EmailMessage(
            'Thanks for your purchase on The Regional Taste',
            template,
            settings.EMAIL_HOST_USER,
            [request.user.email]
        )
        email.fail_silently = False
        email.send()

        context = {'order': order}

        return render(request, 'home/index1.html', context)

    else:
        messages.error(request, "Sorry, you cannot access this data.")
        return redirect("/")
