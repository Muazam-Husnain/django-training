# Generated by Django 3.1.1 on 2020-09-29 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trip_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trip',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='destination_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='destination_location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='host_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='host_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='start_location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='total_days',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_policy',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Itenrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day_number', models.CharField(max_length=3)),
                ('date', models.DateField(null=True)),
                ('places', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_project.trip')),
            ],
        ),
    ]
