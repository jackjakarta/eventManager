# Generated by Django 5.0.2 on 2024-03-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_userapikey"),
    ]

    operations = [
        migrations.AddField(
            model_name="authuser",
            name="is_newsletter_sub",
            field=models.BooleanField(
                default=False,
                help_text="Designates if the user is subscribed to the newsletter.",
                verbose_name="Newsletter Sub",
            ),
        ),
    ]
