""" System Module """
from django import forms
from django_countries.fields import CountryField


class CheckoutForm(forms.Form):
    """
    Create a shipping address form
    """
    address1 = forms.CharField(
        label="Address 1",
        widget=forms.TextInput(attrs={'placeholder': 'Apartment 1'      
    }))
    address2 = forms.CharField(
        label="Address 2",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Dublin'}))
    county = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Dublin'}))
    country = CountryField(blank_label='(select country)').formfield()
    eircode = forms.CharField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
    save_info = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
