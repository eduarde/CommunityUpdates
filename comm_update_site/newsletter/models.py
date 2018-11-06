from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Newsletter(models.Model):
    title = models.CharField(verbose_name="Title", max_length=255)
    date = models.DateField(verbose_name='Date')
    lead = models.CharField(verbose_name='Lead', max_length=100)
    text = models.TextField(verbose_name='text', blank=True)
    flag_image = models.URLField(verbose_name='Flag image', help_text="Paste the url of the image", blank=True)
    image = models.URLField(verbose_name='Image', help_text="Paste the url of the image", blank=True)
    slug = AutoSlugField(populate_from='title')
    virtual_tour_link = models.URLField(verbose_name='URL Virtual Tour', blank=True)
    thank_you_text = models.TextField(verbose_name='Special thank you message', blank=True)

    def get_absolute_url(self):
        return reverse('newsletter_detail', kwargs={'slug': self.slug})

    def get_events(self):
        return self.events

    def get_achievements(self):
        return self.achievemnts

    def __str__(self):
        return "{0} - {1}".format(self.title, self.date)


class SectionAbstract(models.Model):
    title = models.CharField(verbose_name='Title', max_length=140)
    text = models.TextField(verbose_name='text', blank=True)
    read_more_link = models.URLField(verbose_name='Read More', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class AchievementNewslettter(models.Model):
    """
    Through class to handle relationship between Achievement and Newsletter models.
    """
    achievement = models.ForeignKey('Achievement', on_delete=models.CASCADE)
    newsletter = models.ForeignKey('Newsletter', related_name='newsletter_achievement', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        app_label = 'newsletter'
        verbose_name = 'Achievement newsletter'
        verbose_name_plural = 'Achievements newsletter'
        ordering = ('order',)


class Achievement(SectionAbstract):
    image = models.URLField(verbose_name='Image', help_text="Paste the url of the image", blank=True)
    newsletters = models.ManyToManyField(
        'Newsletter', verbose_name="Newsletter",
        through=AchievementNewslettter, related_name='achievemnts', null=True, blank=True)

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
    image = models.URLField(verbose_name='Image', help_text="Paste the url of the image", blank=True)
    newsletters = models.ManyToManyField(
        'Newsletter', verbose_name="Newsletter",
        through=EventNewslettter, related_name='events', null=True, blank=True)


class MemberNewsletter(models.Model):
    newsletter = models.ForeignKey('Newsletter', related_name='newsletter_member', on_delete=models.CASCADE)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        app_label = 'newsletter'
        verbose_name = 'Member newsletter'
        verbose_name_plural = 'Members newsletter'
        ordering = ('order',)


class Member(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=100)
    last_name = models.CharField(verbose_name='Last Name', max_length=140)
    photo = models.URLField(verbose_name='Photo', help_text="Paste the url of the image", blank=True)
    profile_url = models.URLField(verbose_name='UCern Profile URL', blank=True)
    newsletters = models.ManyToManyField(
        'Newsletter', verbose_name="Newsletter",
        through=MemberNewsletter, related_name='member', null=True, blank=True)

    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name
