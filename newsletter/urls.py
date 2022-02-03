from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.newsletter_signup, name='signup'),
    path('unsubscribe/', views.newsletter_unsubscribe, name='unsubscribe'),
]
