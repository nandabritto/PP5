from django import forms
from .models import Product,Product_On_Box
from django.shortcuts import render, get_object_or_404
import logging 

class ProductChoicesForm(forms.Form):
    def __init__(self, pk, *args, **kwargs):
        super(ProductChoicesForm, self).__init__(*args, **kwargs)
        # self.fields['selected_product'].queryset = Product_On_Box.objects.filter(pk=pk)
        # Boxqs = Box.objects.filter(pk=pk)
        PoB = Product_On_Box.objects.filter(box_id=pk)
        Productqs = Product.objects.filter(product_on_box__box_id=pk)
        query = Productqs
        # logging.debug(query)
        # logging.debug(dir(query))
        # # logging.debug(latest(query))
        # logging.debug(query.values())
        self.fields['selected_product'] = forms.ModelChoiceField(queryset=query.all(),widget=forms.CheckboxSelectMultiple)