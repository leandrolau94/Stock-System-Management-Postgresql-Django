# Generated by Django 4.2.2 on 2023-06-29 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_item_acquisition_price_item_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sold_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
