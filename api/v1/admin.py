from django.contrib import admin

from .models import Presentation

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('presentation_id', 'theme')
