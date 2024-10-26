# Generated by Django 5.0.1 on 2024-01-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0020_artist_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="artists",
            field=models.ManyToManyField(
                blank=True, related_name="event_artists", to="website.artist"
            ),
        ),
    ]
