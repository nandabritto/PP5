from django import forms
from django_countries.fields import CountryField

class CheckoutForm(form.Form):
    address1 = forms.CharField(max_length=100, null=True)
    addres2 = forms.CharField(max_length=100, null=True)
    county = forms.CharField(max_length=20, null=True)
    country = CountryField(blank_label='(select country)'))
    eircode = forms.CharField(max_length=7, null=True)
    date_added = forms.DateTimeField(auto_now_add=True)

