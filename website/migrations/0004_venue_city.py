# Generated by Django 5.0.1 on 2024-01-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_venue_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='city',
            field=models.CharField(max_length=120, null=True, verbose_name='Venue City'),
        ),
    ]
