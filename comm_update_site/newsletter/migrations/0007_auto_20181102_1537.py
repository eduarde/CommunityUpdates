# Generated by Django 2.0 on 2018-11-02 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20181102_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementNewslettter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Achievement newsletter',
                'verbose_name_plural': 'Achievements newsletter',
            },
        ),
        migrations.RemoveField(
            model_name='achievement',
            name='newsletter',
        ),
        migrations.AddField(
            model_name='achievementnewslettter',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.Achievement'),
        ),
        migrations.AddField(
            model_name='achievementnewslettter',
            name='newsletter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsletter_achievement', to='newsletter.Newsletter'),
        ),
    ]