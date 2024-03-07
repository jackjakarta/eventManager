# Generated by Django 5.0.2 on 2024-03-07 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_authuser_is_newsletter_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='is_newsletter_sub',
            field=models.BooleanField(default=False, help_text='Check box if you want to subscribe to the newsletter.', verbose_name='Newsletter Sub'),
        ),
    ]
