""" System Module """
from django import forms
from .models import UserProfile, Address


class UserAddressForm(forms.ModelForm):
    """
    Creates an address form for user profile
    """
    class Meta:
        model = Address
        exclude = ('customer', 'default')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'address1': 'Address 1',
            'address2': 'Address 2',
            'county': 'County or City',
            'eircode': 'Eircode',
            'address_type': 'Address',
        }
        

        self.fields['address1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'col-md-6'
            self.fields[field].label = False
