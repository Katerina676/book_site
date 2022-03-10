from django.contrib import admin

from .models import Mail


@admin.register(Mail)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
