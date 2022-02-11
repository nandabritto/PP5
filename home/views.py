""" System Module """
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    """
    A view to return index page 
    """
    return render(request, 'home/index.html')

class Management(TemplateView):
    """ Render management view """
    template_name = 'home/management.html'


class HowItWorksView(TemplateView):
    """ Render how it works view view """
    template_name = 'home/howitworks.html'