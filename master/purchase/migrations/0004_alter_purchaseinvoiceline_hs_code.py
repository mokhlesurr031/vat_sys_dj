# Generated by Django 3.2 on 2022-03-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_auto_20220308_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseinvoiceline',
            name='hs_code',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
