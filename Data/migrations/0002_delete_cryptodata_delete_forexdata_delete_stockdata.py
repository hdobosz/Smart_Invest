# Generated by Django 4.2.7 on 2023-12-20 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CryptoData',
        ),
        migrations.DeleteModel(
            name='ForexData',
        ),
        migrations.DeleteModel(
            name='StockData',
        ),
    ]
