# Generated by Django 2.1.2 on 2018-10-19 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20181019_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='text',
        ),
        migrations.RemoveField(
            model_name='price',
            name='title',
        ),
    ]
