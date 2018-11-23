from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from .views import HomeView, NewsletterView

urlpatterns = [
    url(r'^login/',
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', login_required(HomeView.as_view()), name='home'),
    url(r'^newsletter/(?P<slug>[\w\d\-_]+)/$', login_required(NewsletterView.as_view()), name='newsletter_detail'),
]
