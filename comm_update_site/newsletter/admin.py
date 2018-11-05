from django.contrib import admin
from .models import Newsletter, Achievement, AchievementNewslettter, Event, EventNewslettter, Member, MemberNewsletter
from grappelli.forms import GrappelliSortableHiddenMixin


class TinyMCEMixin(object):
    """
    Used to include tinyMCE text editor in an admin class
    """

    class Media:  # pylint: disable=C1001
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce.js',
        ]


class AchievementsInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    verbose_name = 'Achievement'
    verbose_name_plural = 'Achievements'
    model = AchievementNewslettter
    sortable_field_name = "order"
    extra = 0


class EventsInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    verbose_name = 'Event'
    verbose_name_plural = 'Events'
    model = EventNewslettter
    sortable_field_name = "order"
    extra = 0


class MemberInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    verbose_name = 'Member'
    verbose_name_plural = 'Members'
    model = MemberNewsletter
    sortable_field_name = "order"
    extra = 0


class AchievementsAdmin(TinyMCEMixin, admin.ModelAdmin):
    model = Achievement
    list_display = ('title',)


class NewsletterAdmin(TinyMCEMixin, admin.ModelAdmin):
    model = Newsletter
    list_display = ('title', 'date')
    inlines = (
        AchievementsInline,
        EventsInline,
        MemberInline,
    )


class EventsAdmin(TinyMCEMixin, admin.ModelAdmin):
    model = Event
    list_display = ('title',)


class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ('full_name',)


# Register your models here.
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Achievement, AchievementsAdmin)
admin.site.register(Event, EventsAdmin)
admin.site.register(Member, MemberAdmin)
