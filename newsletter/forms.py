""" System Module """
from django import forms
from .models import NewsletterUser, Newsletter


class NewsLetterUserSignUpForm(forms.ModelForm):
    """
    Creates newsletter signup form
    """
    class Meta:
        """
        Get Newsletter user model to create form
        """
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            """"
            Return user email
            """
            email = self.cleaned_data.get('email')
            return email


class NewsletterCreationForm(forms.ModelForm):
    """
    Creates a form to admin send nesletter
    """

    class Meta:
        """
        Get Newsletter model to create form
        """
        model = Newsletter
        fields = [
            'subject',
            'body',
            'email',
            'status',
        ]
