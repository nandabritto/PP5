from django import forms
from .models import Product

class ProductChoicesForm(forms.Form):
    selected_product = forms.ModelChoiceField(queryset=Product.objects.all(),widget=forms.CheckboxSelectMultiple)