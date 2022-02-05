""" System Module """
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from django.contrib import messages
from django.views.generic import ListView
from .models import NewsletterUser, Newsletter
from .forms import NewsLetterUserSignUpForm, NewsletterCreationForm

def newsletter_signup(request):
    """
    Creates newsletter signup view and get the form
    """
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():            
            # Send email
            subject = "Thank you for joining our newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open("newsletter/templates/newsletter/subscribe_email.txt" ) as f:
                subscribe_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=subscribe_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletter/subscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
            # Message
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
        """
        Unsubscribe user and send confirmation email and message if
        form is valid 
        """
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            # Send email
            subject = "You have been unsubscribe."
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            subscribe_message = "Sorry to see you go. Bye Bye."
            send_mail(subject=subject,
            from_email=from_email, recipient_list=to_email, message=subscribe_message, fail_silently=False)
            # Message
            messages.warning(request, 'Unsubscription completed.')
        else:
            messages.warning(request, 'Sorry, We did not find your email.')

    context = {
        'form': form,
    }
    return render(request, 'newsletter/unsubscribe.html', context)


def send_newsletter(request):
    """
    Save newsletter and send to the  user if form is valid
    """
    if request.method == 'POST':
        form = NewsletterCreationForm(request.POST or None)

        if form.is_valid():            
            instance = form.save()
            newsletter = Newsletter.objects.get(id=instance.id)
            if newsletter.status == 'Published':
                # Send email
                subject = newsletter.subject
                body = newsletter.body
                from_email = settings.EMAIL_HOST_USER
                for email in newsletter.email.all():
                    send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body,
                              fail_silently=True)
                # Message
                messages.success(request, 'Your Changes Write Successfully.')
            else:
                messages.warning(request, 'SomeThing Went Wrong...')
            return redirect('send')
        else:
            form = NewsletterCreationForm(instance=newsletter)

            context = {
                'form': form,
            }
            return render(request, 'newsletter/send_newsletter.html', context)
    else:
        form = NewsletterCreationForm()
    return render(request, 'newsletter/send_newsletter.html', {'form': form})


class NewsletterList(ListView):
    model = Newsletter
    template_name = 'newsletters_list.html'
    paginate_by = 10
    ordering = ['-created']


# def newsletter_list(request):
#     """
#     Create a list of sent newsletter
#     """
#     newsletter = Newsletter.objects.all()
#     paginator = Paginator(newsletters, 10)
#     page = request.GET.get('page')

#     try:
#         items = paginator.page(page)
#     except PageNotAnInteger:
#         items = paginator.page(1)
#     except EmptyPage:
#         items = paginator.page(paginator.num_pages)

    
