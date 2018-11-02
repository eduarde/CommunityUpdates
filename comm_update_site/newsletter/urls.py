from django.conf.urls import url


from .views import HomeView, NewsletterView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^newsletter/(?P<slug>[\w\d\-_]+)/$', NewsletterView.as_view(), name='newsletter_detail'),
]
