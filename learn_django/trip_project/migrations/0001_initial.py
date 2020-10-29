# Generated by Django 3.1.1 on 2020-09-17 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_title', models.CharField(max_length=60)),
                ('trip_description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]