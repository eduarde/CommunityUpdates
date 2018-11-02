from django.contrib import admin
from .models import Newsletter, Achievement
from django.templatetags.static import static


class TinyMCEMixin(object):
    """
    Used to include tinyMCE text editor in an admin class
    """

    class Media:  # pylint: disable=C1001
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce.js',
        ]


class AchievementsInline(TinyMCEMixin, admin.TabularInline):
    verbose_name = 'Achievement'
    verbose_name_plural = 'Achievements'
    model = Achievement
    # form = autocomplete_forms.modelform_factory(ChapterAccordion)
    # sortable_field_name = "order"
    extra = 0


class NewsletterAdmin(TinyMCEMixin, admin.ModelAdmin):
    model = Newsletter
    list_display = ('title', 'date')
    inlines = (
        AchievementsInline,
    )


# Register your models here.
admin.site.register(Newsletter, NewsletterAdmin)
