# Generated by Django 3.1.1 on 2020-12-01 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('trip_project', '0024_auto_20201201_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfigration',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
    ]
