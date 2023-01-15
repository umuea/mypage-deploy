# from django.views.generic import ListView
# from .models import Index


# class HomePageView(ListView):
#     model = Index
#     template_name = "demo/home.html"


from django.shortcuts import render


def main_index(request):
    return render(request, "demo/index.html")
