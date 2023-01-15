# from django.urls import path
# from .views import HomePageView

# urlpatterns = [
#     path("", HomePageView.as_view(), name="home"),
# ]


from django.urls import path
from . import views

app_name = "demo"
urlpatterns = [
    path("", views.demo_index, name="demo_index"),
    path("map_pin", views.demo_mappin, name="demo_mappin"),
]
