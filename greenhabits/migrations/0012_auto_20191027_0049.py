# Generated by Django 2.2.6 on 2019-10-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenhabits', '0011_greenhabitpage_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenhabitpage',
            name='source',
            field=models.CharField(blank=True, help_text='Original author or source. Seek approval of the owner before publishing', max_length=120),
        ),
    ]