# Generated by Django 3.1.1 on 2020-10-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_project', '0004_auto_20201005_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=100)),
                ('host_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='added_by',
            new_name='created_by',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='host_name',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='host_number',
        ),
        migrations.AlterField(
            model_name='trip',
            name='total_days',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
