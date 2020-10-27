# Generated by Django 3.1.1 on 2020-10-27 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip_project', '0016_auto_20201012_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='host_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='host',
            old_name='host_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='trip_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='trip_title',
            new_name='title',
        ),
    ]
