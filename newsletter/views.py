""" System Module """
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import NewsletterUser, Newsletter
from .forms import NewsLetterUserSignUpForm, NewsletterCreationForm


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Create super user only class
    """
    def test_func(self):
        return self.request.user.is_superuser


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
            with open("newsletter/templates/newsletter/subscribe_email.txt") as f:
                subscribe_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject,
                body=subscribe_message,
                from_email=from_email,
                to=to_email
                )
            html_template = get_template(
                "newsletter/subscribe_email.html").render()
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
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            # Send email
            subject = "You have been unsubscribe."
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            subscribe_message = "Sorry to see you go. Bye Bye."
            send_mail(
                subject=subject,
                from_email=from_email,
                recipient_list=to_email,
                message=subscribe_message,
                fail_silently=False
                )
            # Message
            messages.warning(request, 'Unsubscription completed.')
        else:
            messages.warning(request, 'Sorry, We did not find your email.')

    context = {
        'form': form,
    }
    return render(request, 'newsletter/unsubscribe.html', context)


@login_required
def send_newsletter(request):
    """
    Save newsletter and send to the  user if form is valid
    """
    if request.user.is_superuser:
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
                        send_mail(
                            subject=subject,
                            from_email=from_email,
                            recipient_list=[email],
                            message=body,
                            fail_silently=True
                            )
                    # Message
                    messages.success(
                        request, 'Your newsletter was sent.')
                    return redirect('newsletters')
                else:
                    messages.warning(request, 'SomeThing Went Wrong...')
                return redirect('send')
            else:
                form = NewsletterCreationForm(instance=newsletter)

                context = {
                    'form': form,
                }
                return render(
                    request,
                    'newsletter/send_newsletter.html',
                    context)
        else:
            form = NewsletterCreationForm()
        return render(
            request,
            'newsletter/send_newsletter.html',
            {'form': form})
    else:
        messages.error(request, 'Sorry, you do not have permittion \
            to access this page')
        return render(request, 'home/index.html')


class NewsletterList(SuperUserRequiredMixin, ListView):
    """
    Create a list of sent newsletters for admin only
    """
    model = Newsletter
    template_name = 'newsletters_list.html'
    paginate_by = 10
    ordering = ['-created']
