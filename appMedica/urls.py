from django.urls import path
from .views import *

urlpatterns = [
    path("/about", about, name="about"),
    path("/appointment", appointment, name="appointment"),
    path("/blog", blog, name="blog"),
    path("/contact", contact, name="contact"),
    path("/gallery", gallery, name="gallery"),
    path("", home, name="home"),
    path("/services", services, name="services"),
    path("/team", team, name="team")
]
