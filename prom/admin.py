from django.contrib import admin

from .models import PromGuest


class PromGuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'confirmed_presence')
    search_fields = ('first_name', 'last_name')
    list_filter = ('confirmed_presence',)


admin.site.register(PromGuest, PromGuestAdmin)
