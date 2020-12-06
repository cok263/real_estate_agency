from django.contrib import admin

from .models import Flat, Person, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town',)
    list_editable = ('new_building',)
    list_display_links = None
    list_filter = ('new_building', 'rooms_number', 'has_balcony')


class PersonAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('person', 'flat')

admin.site.register(Flat, FlatAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Complaint, ComplaintAdmin)
