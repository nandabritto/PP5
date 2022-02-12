""" System Module """
from crispy_forms.helper import FormHelper
from allauth.account.forms import SignupForm
from django import forms
 
 
class CustomSignupForm(SignupForm):
    """
    Add fields to signup form and reorder them
    """
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    field_order = ['first_name', 'last_name', ' username', 'email',' email2', 'password', 'password2'] 
 
    def __init__(self, *args, **kwargs):
        """
        Remove labels from signup form
        """
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

    def save(self, request):
        """
        Save created data from sigup form
        """
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user