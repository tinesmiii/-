# Generated by Django 4.1.7 on 2023-11-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0007_remove_advertisement_media_advertisement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='advertisements/', verbose_name='Видео'),
        ),
    ]
