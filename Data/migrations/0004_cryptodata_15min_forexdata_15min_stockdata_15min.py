# Generated by Django 4.2.7 on 2023-12-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoData_15min',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('datetime', models.DateTimeField()),
                ('current_price', models.FloatField()),
                ('open_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('percent_change', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ForexData_15min',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('datetime', models.DateTimeField()),
                ('current_price', models.FloatField()),
                ('open_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('percent_change', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StockData_15min',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('datetime', models.DateTimeField()),
                ('current_price', models.FloatField()),
                ('open_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('percent_change', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
    ]
