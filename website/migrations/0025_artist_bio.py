# Generated by Django 5.0.1 on 2024-01-22 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_alter_event_description_alter_event_event_flyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='bio',
            field=models.TextField(blank=True, max_length=700, verbose_name='Artist Bio'),
        ),
    ]