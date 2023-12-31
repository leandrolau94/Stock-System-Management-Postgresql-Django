# Generated by Django 4.1.5 on 2023-06-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('category', models.TextField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('sell_price', models.FloatField()),
                ('created_at', models.DateTimeField()),
                ('modified_at', models.DateTimeField()),
            ],
        ),
    ]
