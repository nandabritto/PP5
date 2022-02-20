""" System Module """
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView


def index(request):
    """
    A view to return index page
    """
    return render(request, 'home/index.html')


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Create staff user only class
    """
    def test_func(self):
        return self.request.user.is_staff


class Management(StaffRequiredMixin, TemplateView):
    """
    A view to return management page for staff users
    """
    template_name = 'home/management.html'


class HowItWorksView(TemplateView):
    """
    A view to return how it works page
    """
    template_name = 'home/howitworks.html'
