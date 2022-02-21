""" System Module """
from django import forms
from django_countries.fields import CountryField


class CheckoutForm(forms.Form):
    """
    Create a shipping address form
    """
    # Shipping address fields
    shipping_address1 = forms.CharField(
        label="Address 1",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Apartment 1'})
        )
    shipping_address2 = forms.CharField(
        label="Address 2",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Dublin'}))
    shipping_county = forms.CharField(
        label="County",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Dublin'}))
    shipping_country = CountryField(
        blank_label='(Select Country)'
        ).formfield(required=False)
    shipping_eircode = forms.CharField(
        label="EirCode",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '123456'}))

    # Billing address fields
    billing_address1 = forms.CharField(
        label="Address 1",
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Apartment 1'})
        )
    billing_address2 = forms.CharField(
        label="Address 2",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Dublin'}))
    billing_county = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Dublin'}))
    billing_country = CountryField(
        blank_label='(Select Country)'
        ).formfield(required=False,)
    billing_eircode = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '123456'}))

    # Options fields
    same_billing_address = forms.BooleanField(
        label="Billing address is the same as my shipping address",
        widget=forms.CheckboxInput(), required=False)
    set_default_shipping = forms.BooleanField(
        label="Save this address as my default for shipping",
        required=False)
    use_default_shipping = forms.BooleanField(
        label="Use my default shipping address",
        required=False)
    set_default_billing = forms.BooleanField(
        label="Save this address as my default for billing",
        required=False)
    use_default_billing = forms.BooleanField(
        label="Use my default billing address",
        required=False)
