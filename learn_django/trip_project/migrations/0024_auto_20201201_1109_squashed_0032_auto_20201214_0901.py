# Generated by Django 3.1.1 on 2020-12-14 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('trip_project', '0024_auto_20201201_1109'), ('trip_project', '0025_auto_20201201_1118'), ('trip_project', '0026_auto_20201201_1120'), ('trip_project', '0027_auto_20201201_1122'), ('trip_project', '0028_auto_20201201_1123'), ('trip_project', '0029_auto_20201211_1027'), ('trip_project', '0030_auto_20201211_1111'), ('trip_project', '0031_auto_20201214_0647'), ('trip_project', '0032_auto_20201214_0901')]

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('trip_project', '0023_siteconfigration_add_trip_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfigration',
            name='add_trip_url',
        ),
        migrations.AddField(
            model_name='siteconfigration',
            name='values',
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='siteconfigration',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
        migrations.AlterField(
            model_name='siteconfigration',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='siteconfiguration', to='sites.site'),
        ),
        migrations.AlterField(
            model_name='siteconfigration',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='siteconfigration', to='sites.site'),
        ),
        migrations.AlterField(
            model_name='siteconfigration',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name='trip',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='trip',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='TripSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('over_ridden_price', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateField()),
                ('is_active', models.BooleanField(default=1)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_project.trip')),
            ],
        ),
        migrations.RemoveField(
            model_name='trip',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='trip',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
