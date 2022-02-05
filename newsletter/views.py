""" System Module """
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
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
            subject = "Thank you for joining our newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open("newsletter/templates/newsletter/subscribe_email.txt" ) as f:
                subscribe_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=subscribe_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletter/subscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
            messages.warning(request, 'You have already signed up')
        else:
            instance.save()
            messages.success(request, 'You have signed up.')
        
    context = {
        'form': form,
    }
    return render(request, 'newsletter/subscribe.html', context)


def newsletter_unsubscribe(request):
    """
    Creates newsletter unsubscribe view and get the form
    """
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            subject = "You have been unsubscribe."
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open("newsletter/templates/newsletter/unsubscribe_email.txt" ) as f:
                subscribe_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=subscribe_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletter/unsubscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
            messages.warning(request, 'Unsubscription completed.')     
        else:
            messages.warning(request, 'Sorry, We did not find your email.')

    context = {
        'form': form,
    }
    return render(request, 'newsletter/unsubscribe.html', context)
