# Generated by Django 5.0.1 on 2024-01-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0019_alter_venue_address_alter_venue_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="artist",
            name="image",
            field=models.ImageField(
                default=None, upload_to="artist_images/", verbose_name="Artist Image"
            ),
        ),
    ]
