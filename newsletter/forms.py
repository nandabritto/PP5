""" System Module """
from django import forms
from .models import NewsletterUser, Newsletter

class NewsLetterUserSignUpForm(forms.ModelForm):
    """
    Creates newsletter signup form
    """
    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email

class NewsletterCreationForm(forms.ModelForm):
    """
    Creates a newsletter form 
    """
    class Meta:
        model = Newsletter
        fields = [
            'subject',
            'body',
            'email',
            'status'
        ]
    
