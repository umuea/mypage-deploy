# from django.views.generic import ListView
# from .models import Index


# class HomePageView(ListView):
#     model = Index
#     template_name = "demo/home.html"


from django.shortcuts import render
import folium


def demo_index(request):
    return render(request, "demo/index.html")


def demo_mappin(request):
    m = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
    tooltip = "Click me!"

    folium.Marker(
        [45.3288, -121.6625], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip
    ).add_to(m)
    folium.Marker(
        [45.3311, -121.7113], popup="<b>Timberline Lodge</b>", tooltip=tooltip
    ).add_to(m)
    map = m._repr_html_()
    context = {
        "map": map,
    }
    return render(request, "demo/mappin.html", context)
