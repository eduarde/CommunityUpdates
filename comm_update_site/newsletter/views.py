from django.views.generic import ListView, DetailView
from .models import Newsletter
from django.shortcuts import get_list_or_404, get_object_or_404

class HomeView(ListView):

    model = Newsletter
    template_name = 'home.html'
    context_object_name = 'newsletters'


class NewsletterView(DetailView):

    model = Newsletter
    template_name = 'newsletter.html'
    context_object_name = 'newsletter'

    def get_object(self, queryset=None):
        return get_object_or_404(Newsletter, slug=self.kwargs.get('slug', None))

