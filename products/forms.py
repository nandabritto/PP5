""" System Module """
from django import forms
from .models import Product


class ProductChoicesForm(forms.Form):
    """
    Create checkboxes to add products on box
    """
    def __init__(self, pk, *args, **kwargs):
        """
        Get objects on prooducts model, filter by box and create checkboxes
        """
        super(ProductChoicesForm, self).__init__(*args, **kwargs)
        query = Product.objects.filter(product_on_box__box_id=pk)
        self.fields['selected_product'] = forms.ModelChoiceField(
            queryset=query.all(), widget=forms.CheckboxSelectMultiple, empty_label=None)
        self.fields['selected_product'].label = False
