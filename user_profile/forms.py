from django import forms
from .models import UserProfile, Address


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ('customer','default')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'address1': 'Address 1',
            'address2': 'Address 2',
            'county': 'County or City',
            'country': 'Country',
            'eircode': 'Eircode',
            'address_type': 'Address',

        }

        self.fields['address1'].widget.attrs['autofocus'] = True
        print(self.fields)
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False

# class UserShippingAddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         exclude = ('customer','default')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         placeholders = {
#             'address1': 'Address 1',
#             'address2': 'Address 2',
#             'county': 'County or City',
#             'country': 'Country',
#             'eircode': 'Eircode',
#             'address_type': 'Address',

#         }

#         self.fields['address1'].widget.attrs['autofocus'] = True
#         print(self.fields)
#         for field in self.fields:
#             if field != 'country':
#                 if self.fields[field].required:
#                     placeholder = f'{placeholders[field]} *'
#                 else:
#                     placeholder = placeholders[field]
#                 self.fields[field].widget.attrs['placeholder'] = placeholder
#             # self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
#             self.fields[field].label = False


# class UserBillingAddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         exclude = ('customer','default')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         placeholders = {
#             'address1': 'Address 1',
#             'address2': 'Address 2',
#             'county': 'County or City',
#             'country': 'Country',
#             'eircode': 'Eircode',
#             'address_type': 'Billing Address',

#         }

#         self.fields['address1'].widget.attrs['autofocus'] = True
#         print(self.fields)
#         for field in self.fields:
#             if field != 'country':
#                 if self.fields[field].required:
#                     placeholder = f'{placeholders[field]} *'
#                 else:
#                     placeholder = placeholders[field]
#                 self.fields[field].widget.attrs['placeholder'] = placeholder
#             # self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
#             self.fields[field].label = False

