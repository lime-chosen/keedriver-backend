# Generated by Django 4.2.4 on 2023-09-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire_us', '0008_remove_driverreport_trip_id_hiretripreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiretrips',
            name='trip_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hiretrips',
            name='trip_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]