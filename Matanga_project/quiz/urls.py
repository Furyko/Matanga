from django.urls import path

from . import views

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    #path('juego/', views.juego, name='juego'),
    path('mapa/', views.mapa, name='mapa'),
    path('ranking/', views.ranking, name='ranking'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('registro/', views.registro, name='registro'),
    path('', views.inicio, name='inicio'),
    path('cerarSesion/', views.cerrarSesion, name="cerrarSesion"),

    path('derrota/<int:id_partida>', views.derrota, name='derrota'),
    path('victoria/<int:id_partida>', views.victoria, name='victoria'),
    
    #Aquí impactan los FORMS
    path('juego/<int:id_partida>', views.juego, name='juego'),
    path('mapa/<int:id_usuario>', views.mapa, name='mapa'),
]