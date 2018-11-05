# Generated by Django 2.0 on 2018-11-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0014_auto_20181102_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='read_more_link',
            field=models.URLField(blank=True, verbose_name='Read More'),
        ),
        migrations.AddField(
            model_name='event',
            name='read_more_link',
            field=models.URLField(blank=True, verbose_name='Read More'),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='virtual_tour_link',
            field=models.URLField(blank=True, verbose_name='URL Virtual Tour'),
        ),
    ]
