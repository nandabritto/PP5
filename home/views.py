""" System Module """
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    """
    A view to return index page
    """
    return render(request, 'home/index.html')


class Management(TemplateView):
    """
    A view to return mnagement page
    """
    template_name = 'home/management.html'


class HowItWorksView(TemplateView):
    """
    A view to return how it works page
    """
    template_name = 'home/howitworks.html'
