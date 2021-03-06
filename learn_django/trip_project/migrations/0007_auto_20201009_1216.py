# Generated by Django 3.1.1 on 2020-10-09 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip_project', '0006_trip_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locattion_name', models.CharField(choices=[('NR', 'Naran'), ('HN', 'Hunza'), ('SK', 'Skardu'), ('LHE', 'Lahore'), ('ISB', 'Islamabad')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='itenrary',
            name='date',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='destination_date',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='total_days',
        ),
        migrations.AddField(
            model_name='trip',
            name='destination_location_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trip_project.locations'),
        ),
        migrations.AddField(
            model_name='trip',
            name='start_location_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_location', to='trip_project.locations'),
        ),
    ]
