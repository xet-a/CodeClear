from django.urls import path, include
from . import views

app_name = "life"

urlpatterns = [
    path("main/", views.index, name="main"),
]