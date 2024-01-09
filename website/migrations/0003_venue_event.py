# Generated by Django 5.0.1 on 2024-01-08 16:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=250, verbose_name='Venue Address')),
                ('zip_code', models.CharField(max_length=20, verbose_name='Zip Code')),
                ('website', models.URLField(verbose_name='Venue Website')),
                ('email', models.EmailField(max_length=254, verbose_name='Venue Email')),
            ],
            options={
                'db_table': 'venues',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('event_flyer', models.ImageField(default=None, upload_to='event_flyers/', verbose_name='Event Flyer')),
                ('description', models.TextField(blank=True)),
                ('attendees', models.ManyToManyField(blank=True, related_name='attended_events', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.venue')),
            ],
            options={
                'db_table': 'events',
            },
        ),
    ]
