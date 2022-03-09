from unicodedata import name
from django.urls import path

from . import views

app_name='antaganize'
urlpatterns = [
    path('', views.view_index, name='index'),
    path('help/', views.view_help, name='help'),
    path('about/', views.view_about, name='about')
]