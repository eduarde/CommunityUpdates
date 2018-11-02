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

    def __unicode__(self):
        return "{0} - {1}".format(self.title, self.date)


class Achievement(models.Model):

    newsletter = models.ForeignKey('Newsletter', related_name='newsletter_item', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Date')
    title = models.CharField(verbose_name='Title', max_length=140)
    text = models.TextField(verbose_name='text', blank=True)
    image = FileBrowseField('Image', max_length=100, directory="flags",
                            extensions=['.jpg', '.jpeg', '.gif', '.png'], blank=True, null=True)

    def __unicode__(self):
        return self.title

