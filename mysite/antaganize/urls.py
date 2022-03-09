from unicodedata import name
from django.urls import path

from . import views

app_name='antaganize'
urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about')
]