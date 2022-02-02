from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    # path('update_shipping', views.update_shipping, name='update_shipping'),

]

