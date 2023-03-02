# Generated by Django 4.1.6 on 2023-03-01 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0002_alter_city_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Username')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='e-mail')),
                ('phone', models.CharField(max_length=30, unique=True, verbose_name='phone number')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='last name')),
                ('country', models.CharField(blank=True, max_length=5, null=True, verbose_name='country')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('is_customer', models.BooleanField(default=False, verbose_name='Customer')),
                ('is_driver', models.BooleanField(default=False, verbose_name='Driver')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.myuser',),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.myuser',),
        ),
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('license_number', models.CharField(blank=True, max_length=50, null=True)),
                ('aadhaar_number', models.CharField(blank=True, max_length=20, null=True)),
                ('is_avaliable', models.BooleanField(default=False)),
                ('area', models.ManyToManyField(to='areas.area')),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.driver')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_business', models.BooleanField(default=False)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
    ]
