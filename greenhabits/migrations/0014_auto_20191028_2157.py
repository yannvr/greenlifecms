# Generated by Django 2.2.5 on 2019-10-28 21:57

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('greenhabits', '0013_auto_20191028_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='GreenHabitTagPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='greenhabitpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='greenhabits.GreenHabitTagPage', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='GreenHabitPageTag',
        ),
        migrations.AddField(
            model_name='greenhabittagpage',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='greenhabits.GreenHabitPage'),
        ),
        migrations.AddField(
            model_name='greenhabittagpage',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='greenhabits_greenhabittagpage_items', to='taggit.Tag'),
        ),
    ]
