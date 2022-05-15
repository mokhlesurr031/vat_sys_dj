# Generated by Django 3.2 on 2022-05-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_saleinvoiceline_cd_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleinvoiceline',
            name='ait_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='saleinvoiceline',
            name='atv_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='saleinvoiceline',
            name='rd_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='saleinvoiceline',
            name='sd_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='saleinvoiceline',
            name='tti',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='saleinvoiceline',
            name='tti_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='saleinvoiceline',
            name='vat_amount',
            field=models.FloatField(default=0),
        ),
    ]
