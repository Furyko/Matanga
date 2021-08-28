from django.urls import path

from . import views

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('fin/', views.fin, name='fin'),
    path('juego/', views.juego, name='juego'),
    path('mapa/', views.mapa, name='mapa'),
    path('ranking/', views.ranking, name='ranking'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('registro/', views.registro, name='registro'),
    path('victoria/', views.victoria, name='victoria'),
    path('', views.inicio, name='inicio'),
    path('cerarSesion/', views.cerrarSesion, name="cerrarSesion"),
]