# Generated by Django 3.2 on 2022-05-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220308_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='hscode',
            name='tti',
            field=models.FloatField(default=0),
        ),
    ]