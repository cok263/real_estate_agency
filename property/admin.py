from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town',)
    list_editable = ('new_building',)
    list_display_links = None


admin.site.register(Flat, FlatAdmin)
