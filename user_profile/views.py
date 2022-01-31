from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Order, OrderBox
from .forms import UserProfileForm
from .models import UserProfile


def profile(request):
    profile = get_object_or_404(UserProfile, customer=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile was updated.')
        else:
            messages.error(request, ' Form invalid')
    
    form = UserProfileForm(instance=profile)
    ordered_boxes = profile.ordered_boxes.all()
    template = 'user_profile/profiles.html'
    context = {
        'form': form,
        'ordered_boxes': ordered_boxes,
    }
    return render(request, template, context)

