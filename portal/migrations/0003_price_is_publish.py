# Generated by Django 2.1.2 on 2018-10-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20181015_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
    ]
