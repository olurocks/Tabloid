from django.shortcuts import render
from django.views.generic import ListView
from .models import Episode, Content

class HomePageView(ListView):
    template_name ="homepage.html"
    model = Episode

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by("-pub_date")[:20]

        return context

class VanguardView(ListView):
    template_name = "vanguard.html"
    model = Content
    
    def get_context_data(self, **kwargs):
        setup =super().get_context_data(**kwargs)
        setup["contents"] = Content.objects.filter().order_by("-pub_date")[:20]

        return setup
    

# Create your views here.
