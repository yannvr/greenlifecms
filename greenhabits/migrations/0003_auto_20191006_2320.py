# Generated by Django 2.2.6 on 2019-10-06 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenhabits', '0002_auto_20191006_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenhabitpage',
            name='header',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
