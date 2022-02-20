""" System Module """
from allauth.account.forms import SignupForm, LoginForm
from django import forms


class CustomSignupForm(SignupForm):
    """
    Add fields to signup form and reorder them
    """
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(
        max_length=30, label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    field_order = ['first_name', 'last_name']

    def save(self, request):
        """
        Save created data from sigup form
        """
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class CustomLoginForm(LoginForm):
    """
    Change label from login
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].label = "Username"
        self.fields["password"].label = "Password"
