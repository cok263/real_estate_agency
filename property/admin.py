from django.contrib import admin

from .models import Flat, Person, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by', 'owners')


class PersonAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'liked_flats')


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('person', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'pure_phone')
    raw_id_fields = ('flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
