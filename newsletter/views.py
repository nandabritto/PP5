""" System Module """
from django.shortcuts import render
from django.contrib import messages
from .models import NewsletterUser
from .forms import NewsLetterUserSignUpForm

def newsletter_signup(request):
    """
    Creates newsletter signup view and get the form
    """
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'You have already signed up')
        else:
            instance.save()
            messages.success(request, 'You have signed up.')

    context = {
        'form': form,
    }
    return render(request, 'newsletter/signup.html', context)


def newsletter_unsubscribe(request):
    """
    Creates newsletter unsubscribe view and get the form
    """
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exist():
            NewsletterUser.objects.filter(email=instance.email).delete()
        else:
            messages.warning(request, 'Sorry, We did not find your email.')

    context = {
        'form': form,
    }
    return render(request, 'newsletter/unsubscribe.html', context)

