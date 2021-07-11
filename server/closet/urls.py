from django.urls import path, include, re_path
from . import views

app_name = 'closet'

urlpatterns = [
    path('', views.index),
    #url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
    path('closet/create', views.closet_create, name='closet_create'),
]