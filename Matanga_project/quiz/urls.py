from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('fin', views.fin, name='fin'),
    path('mapa/<pk>/', views.juego, name='juego'),
    path('mapa', views.mapa, name='mapa'),
    path('ranking', views.ranking, name='ranking'),
    path('recuperar', views.recuperar, name='recuperar'),
    path('registro', views.registro, name='registro'),
    path('victoria', views.victoria, name='victoria'),
    path('', views.inicio, name='inicio'),
]