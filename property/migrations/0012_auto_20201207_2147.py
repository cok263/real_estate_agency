# Generated by Django 2.2.4 on 2020-12-07 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20201207_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
