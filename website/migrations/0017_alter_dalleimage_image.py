# Generated by Django 5.0.1 on 2024-01-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0016_apikey"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dalleimage",
            name="image",
            field=models.ImageField(
                upload_to="generated_images/<django.db.models.query_utils.DeferredAttribute object at 0x105dcd010>/",
                verbose_name="Generated Image",
            ),
        ),
    ]
