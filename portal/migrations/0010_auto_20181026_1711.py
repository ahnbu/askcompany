# Generated by Django 2.1.2 on 2018-10-26 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_price_discount_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={},
        ),
        migrations.AlterField(
            model_name='price',
            name='discount_price',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]