# Generated by Django 2.2.4 on 2020-12-06 19:34

from django.db import migrations


class Migration(migrations.Migration):

    def make_owner(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        Owner = apps.get_model('property', 'Owner')
        for flat in Flat.objects.all():
            owner, created = Owner.objects.get_or_create(
                name=flat.owner,
                pure_phone=flat.owner_pure_phone,
                defaults={
                    'phonenumber': flat.owners_phonenumber,
                }
            )


    def move_backward(apps, schema_editor):
        Owner = apps.get_model('property', 'Owner')
        Owner.objects.all().delete()


    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(make_owner, move_backward)
    ]
