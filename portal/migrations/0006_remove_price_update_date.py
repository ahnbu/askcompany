# Generated by Django 2.1.2 on 2018-10-19 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20181019_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='update_date',
        ),
    ]
