# Generated by Django 2.2.4 on 2020-11-24 22:00

from django.db import migrations


class Migration(migrations.Migration):

    def update_new_building_field(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        for flat in Flat.objects.all():
            if flat.construction_year >= 2015:
                flat.new_building = True
                flat.save()
            else:
                flat.new_building = False
                flat.save()


    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(update_new_building_field),
    ]
