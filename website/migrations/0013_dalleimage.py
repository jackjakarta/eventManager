# Generated by Django 5.0.1 on 2024-01-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='DallEImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=120, verbose_name='Image Title')),
                ('image', models.ImageField(upload_to='generated_images', verbose_name='Generated Image')),
            ],
            options={
                'db_table': 'dall_e_generated_images',
            },
        ),
    ]
