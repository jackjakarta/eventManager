# Generated by Django 5.0.1 on 2024-01-15 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0022_promoter_image"),
    ]

    operations = [
        migrations.DeleteModel(
            name="APIKey",
        ),
    ]
