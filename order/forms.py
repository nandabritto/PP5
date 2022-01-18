from django import forms
from django_countries.fields import CountryField

class CheckoutForm(forms.Form):
    address1 = forms.CharField()
    address2 = forms.CharField(required=False)
    county = forms.CharField()
    country = CountryField(blank_label='(select country)')
    eircode = forms.CharField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.BooleanField(widget=forms.RadioSelect())
 

