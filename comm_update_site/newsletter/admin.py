from django.contrib import admin
from .models import Newsletter, Achievement, AchievementNewslettter
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


class AchievementsAdmin(TinyMCEMixin, admin.ModelAdmin):
    model = Achievement
    list_display = ('title',)


class NewsletterAdmin(TinyMCEMixin, admin.ModelAdmin):
    model = Newsletter
    list_display = ('title', 'date')
    inlines = (
        AchievementsInline,
    )


# Register your models here.
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Achievement, AchievementsAdmin)
