# Generated by Django 3.2 on 2023-05-18 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parties',
            name='email',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
