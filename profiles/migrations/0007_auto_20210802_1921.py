# Generated by Django 3.2.5 on 2021-08-02 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210802_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_phone_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_postcode',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_street_address1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_street_address2',
        ),
    ]
