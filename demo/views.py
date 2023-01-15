from django.views.generic import ListView
from .models import Index


class HomePageView(ListView):
    model = Index
    template_name = "demo/home.html"
