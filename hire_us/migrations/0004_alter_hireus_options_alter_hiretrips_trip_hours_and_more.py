# Generated by Django 4.2.4 on 2023-09-07 04:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_driverprofile_license_expiry_date_and_more'),
        ('hire_us', '0003_alter_hiretrips_trip_hours'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hireus',
            options={'verbose_name': 'Hire us', 'verbose_name_plural': 'Hire us'},
        ),
        migrations.AlterField(
            model_name='hiretrips',
            name='trip_hours',
            field=models.DurationField(default=datetime.timedelta(seconds=7200), null=True),
        ),
        migrations.CreateModel(
            name='HireusReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_title', models.CharField(max_length=255)),
                ('billing_start_date', models.DateField()),
                ('billing_end_date', models.DateField()),
                ('trip_count', models.IntegerField()),
                ('trip_attended', models.IntegerField()),
                ('amount_per_day', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('amount_status', models.CharField(choices=[('NOT PAID', 'Not Paid'), ('PAID', 'Paid')], default='NOT PAID', max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hire', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hire_us.hireus')),
            ],
        ),
        migrations.CreateModel(
            name='DriverReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_working_hours', models.DurationField()),
                ('driver_trip_count', models.IntegerField()),
                ('driver_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.driver')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hire_us.hireusreport')),
            ],
        ),
    ]