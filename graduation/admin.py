from django.contrib import admin
from django.utils.html import format_html

from .models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('picture_preview',)

    @staticmethod
    def picture_preview(obj):
        if obj.picture:
            return format_html(
                f'<img src="{obj.picture.url}" style="max-width: 100px; max-height: 100px;" />'  # noqa: E501
            )
        return '-'

    picture_preview.short_description = 'Pré-visualização da Foto'
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


admin.site.register(Guest, GuestAdmin)
