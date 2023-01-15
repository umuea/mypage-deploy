# from django.urls import path
# from .views import HomePageView

# urlpatterns = [
#     path("", HomePageView.as_view(), name="home"),
# ]


from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.main_index, name="main_index"),
]
