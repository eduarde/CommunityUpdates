# Generated by Django 2.0 on 2018-11-02 10:34

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20181102_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('title', models.CharField(max_length=140, verbose_name='Title')),
                ('text', models.TextField(blank=True, verbose_name='text')),
                ('image', filebrowser.fields.FileBrowseField(blank=True, max_length=100, null=True, verbose_name='Image')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsletter_item', to='newsletter.Newsletter')),
            ],
        ),
    ]
