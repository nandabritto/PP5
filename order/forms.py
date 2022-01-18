from django import forms
from django_countries.fields import CountryField

class CheckoutForm(form.Form):
    address1 = forms.CharField(max_length=100, null=True)
    address2 = forms.CharField(max_length=100, null=True, required=False)
    county = forms.CharField(max_length=20, null=True)
    country = CountryField(blank_label='(select country)'))
    eircode = forms.CharField(max_length=7, null=True)
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=CheckboxInput())
    payment_option = forms.BooleanField(widget=forms.RadioSelect())
    date_added = forms.DateTimeField(auto_now_add=True)

