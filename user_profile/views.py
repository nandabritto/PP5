from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def profile(request):
    template = 'user_profile/profiles.html'
    context = {}

    return render(request, template, context)

