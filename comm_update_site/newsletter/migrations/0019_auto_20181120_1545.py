# Generated by Django 2.0 on 2018-11-20 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0018_auto_20181106_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalThought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Title')),
                ('text', models.TextField(blank=True, verbose_name='text')),
                ('read_more_link', models.URLField(blank=True, verbose_name='Read More')),
                ('image', models.URLField(blank=True, help_text='Paste the url of the image', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Final thought',
                'verbose_name_plural': 'Final thoughts',
            },
        ),
        migrations.CreateModel(
            name='FinalThoughtNewsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
                ('finalthought', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.FinalThought')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsletter_finalthought', to='newsletter.Newsletter')),
            ],
            options={
                'verbose_name': 'Final thought newsletter',
                'verbose_name_plural': 'Final thoughts newsletter',
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='finalthought',
            name='thoughts',
            field=models.ManyToManyField(blank=True, null=True, related_name='finalthoughts', through='newsletter.FinalThoughtNewsletter', to='newsletter.FinalThought', verbose_name='Thoughts'),
        ),
    ]