# Generated by Django 4.1.7 on 2023-11-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0013_delete_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='right_answer',
            field=models.IntegerField(default=1, verbose_name='Верный ответ'),
        ),
    ]
