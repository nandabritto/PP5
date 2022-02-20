""" System Module """
from django import forms
from .models import Product, Box, ProductOnBox


class ProductChoicesForm(forms.Form):
    """
    Create checkboxes to add products on box
    """
    def __init__(self, pk, *args, **kwargs):
        """
        Get objects on prooducts model, filter by box and create checkboxes
        """
        super(ProductChoicesForm, self).__init__(*args, **kwargs)
        query = Product.objects.filter(productonbox__box_id=pk)
        selectables_query = query.filter(
            productonbox__product_selectable=True)
        self.fields['selected_product'] = forms.ModelChoiceField(
            queryset=selectables_query.all(),
            widget=forms.CheckboxSelectMultiple,
            empty_label=None)
        self.fields['selected_product'].label = False


class BoxForm(forms.ModelForm):
    """
    Create Products form
    """
    class Meta:
        """
        Get Box model and add widgets to fields
        """
        model = Box
        fields = '__all__'
        widgets = {
          'box_description': forms.Textarea(attrs={'rows': 4}),
          'box_note2': forms.Textarea(attrs={'rows': 2}),
          'box_note1': forms.Textarea(attrs={'rows': 2}),
        }


class ProductForm(forms.ModelForm):
    """
    Create Box form
    """
    class Meta:
        """
        Get Product model and add widgets to fields
        """
        model = Product
        fields = '__all__'
        widgets = {
          'product_description': forms.Textarea(attrs={'rows': 4}),
          'product_note1': forms.Textarea(attrs={'rows': 2}),
          'product_note2': forms.Textarea(attrs={'rows': 2})
        }


class ProductOnBoxForm(forms.ModelForm):
    """
    Add products on boxes form
    """
    class Meta:
        """
        Get Product on Box model
        """
        model = ProductOnBox
        fields = '__all__'
