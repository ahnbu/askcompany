# Generated by Django 2.1.2 on 2018-10-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_price_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='discount_price',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
