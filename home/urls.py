""" System Module """
from django.urls import path
from .views import Management, HowItWorksView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('management/', Management.as_view(), name='management'),
    path('howitworks/', HowItWorksView.as_view(), name='howitworks'),
]
