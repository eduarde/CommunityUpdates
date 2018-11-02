from django.db import models
from filebrowser.fields import FileBrowseField


# Create your models here.
class Newsletter(models.Model):
    title = models.CharField(verbose_name="Title", max_length=255)
    date = models.DateField(verbose_name='Date')
    lead = models.CharField(verbose_name='Lead', max_length=100)
    text = models.TextField(verbose_name='text', blank=True)
    image = FileBrowseField('Image', max_length=100, directory="flags",
                            extensions=['.jpg', '.jpeg', '.gif', '.png'], blank=True, null=True)

    def __str__(self):
        return "{0} - {1}".format(self.title, self.date)


class SectionAbstract(models.Model):

    title = models.CharField(verbose_name='Title', max_length=140)
    text = models.TextField(verbose_name='text', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class AchievementNewslettter(models.Model):
    """
    Through class to handle relationship between Achievement and Newsletter models.
    """
    newsletter = models.ForeignKey('Newsletter', related_name='newsletter_achievement', on_delete=models.CASCADE)
    achievement = models.ForeignKey('Achievement', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        app_label = 'newsletter'
        verbose_name = 'Achievement newsletter'
        verbose_name_plural = 'Achievements newsletter'
        ordering = ('order',)


class Achievement(SectionAbstract):

    image = FileBrowseField('Image', max_length=100, directory="achievements",
                            extensions=['.jpg', '.jpeg', '.gif', '.png'], blank=True, null=True)

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'


class EventNewslettter(models.Model):
    """
    Through class to handle relationship between Event and Newsletter models.
    """
    newsletter = models.ForeignKey('Newsletter', related_name='newsletter_event', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        app_label = 'newsletter'
        verbose_name = 'Event newsletter'
        verbose_name_plural = 'Events newsletter'
        ordering = ('order',)


class Event(SectionAbstract):
    date = models.DateField(verbose_name='Date')
    image = FileBrowseField('Image', max_length=100, directory="events",
                            extensions=['.jpg', '.jpeg', '.gif', '.png'], blank=True, null=True)








