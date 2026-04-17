from django.contrib import admin

from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'branch', 'created_at')
    list_filter = ('branch', 'created_at')
    search_fields = ('full_name', 'phone', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
