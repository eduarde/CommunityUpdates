# Generated by Django 2.0 on 2018-11-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0013_auto_20181102_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='newsletters',
            field=models.ManyToManyField(blank=True, null=True, related_name='achievemnts', through='newsletter.AchievementNewslettter', to='newsletter.Newsletter', verbose_name='Newsletter'),
        ),
        migrations.AddField(
            model_name='event',
            name='newsletters',
            field=models.ManyToManyField(blank=True, null=True, related_name='events', through='newsletter.EventNewslettter', to='newsletter.Newsletter', verbose_name='Newsletter'),
        ),
    ]
