from django.db import models
from django.db.models.fields import CharField, DateField, DateTimeField, IntegerField
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

import datetime
import threading


class Partida(models.Model):
    puntaje_maximo= models.IntegerField(blank=True, null=True)
    puntaje_juego= models.IntegerField(blank=True, null=True)
    victoria= models.BooleanField(blank=True, null=True, default=False)
    personaje = models.CharField(blank=True, null=True, max_length=50,  default='gaucho')

    id_fecha = models.ForeignKey('fecha', models.DO_NOTHING, db_column='id_fecha', blank=True, null=True)
    
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    
    id_categoria = models.ForeignKey('categoria', models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    id_dificultad = models.ForeignKey('dificultad', models.DO_NOTHING, db_column='id_dificultad', blank=True, default=2) 
    #ID 2 es normal en dificultad
   

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, blank=True, null=True)
    
class Fecha(models.Model):
    date = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)

class Quiz(models.Model):
    id_categoria = models.ForeignKey('categoria', models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    pregunta = models.CharField(max_length=250, blank=True, null=True)
    respuesta_1 = models.CharField(max_length=200, blank=True, null=True)
    correcto_1= models.BooleanField(default=False)
    respuesta_2 = models.CharField(max_length=200, blank=True, null=True)
    correcto_2= models.BooleanField(default=False)
    respuesta_3 = models.CharField(max_length=200, blank=True, null=True)
    correcto_3= models.BooleanField(default=False)
    respuesta_4 = models.CharField(max_length=200, blank=True, null=True)
    correcto_4= models.BooleanField(default=False)
    respuesta_5 = models.CharField(max_length=200, blank=True, null=True)
    correcto_5= models.BooleanField(default=False)

    def __str__(self):
            return str(self.pregunta)


class Dificultad(models.Model):
    informacion = CharField(max_length=20, blank=True, null=True)
    vida = IntegerField(blank=True, null=True)
    tiempo= IntegerField(blank=True, null=True)
    cant_respuestas = IntegerField(blank=True, null=True)
    
    
    

