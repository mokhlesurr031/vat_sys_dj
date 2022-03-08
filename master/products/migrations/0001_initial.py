# Generated by Django 3.2 on 2022-03-08 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HSCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hs_code', models.CharField(max_length=155)),
                ('description', models.CharField(max_length=455)),
                ('uom', models.CharField(choices=[('number', 'NMB'), ('kg', 'KGM')], max_length=25)),
                ('cd', models.FloatField()),
                ('sd', models.FloatField()),
                ('vat', models.FloatField()),
                ('ait', models.FloatField()),
                ('rd', models.FloatField()),
                ('atv', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('hs_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.hscode')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('product_type', models.CharField(choices=[('raw_material', 'Raw Material'), ('finished_good', 'Finished Good')], max_length=200)),
                ('purchase_price', models.FloatField()),
                ('sale_price', models.FloatField()),
                ('available_in_po', models.BooleanField(default=0)),
                ('available_in_so', models.BooleanField(default=0)),
                ('description', models.TextField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productvariant')),
            ],
        ),
    ]
