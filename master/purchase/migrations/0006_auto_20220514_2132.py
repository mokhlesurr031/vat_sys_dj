# Generated by Django 3.2 on 2022-05-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0005_purchaseinvoice_invoice_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseinvoiceline',
            name='ait_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='purchaseinvoiceline',
            name='atv_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='purchaseinvoiceline',
            name='cd_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='purchaseinvoiceline',
            name='rd_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='purchaseinvoiceline',
            name='sd_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='purchaseinvoiceline',
            name='tti',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='purchaseinvoiceline',
            name='tti_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='purchaseinvoiceline',
            name='vat_amount',
            field=models.FloatField(default=0),
        ),
    ]