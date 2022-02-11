"""System Module """
from django.contrib import admin
from .models import NewsletterUser, Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    """
    Display a list of information about newsletter
    """
    list_display = ('email', 'date_added',)


admin.site.register(NewsletterUser, NewsletterAdmin)
admin.site.register(Newsletter)
