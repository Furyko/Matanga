from django.db import models
from django.db.models.fields import DateField, DateTimeField, IntegerField
from django.utils import timezone
from django.contrib.auth.models import User


DIFICULTAD_RESPUESTAS = (
    ('facil', 'facil'),
    ('intermedio', 'intermedio'),
    ('dificil', 'dificil'),
)


class Usuario(models.Model):
    nombre= models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    clave= models.CharField(max_length=100)
    admin = models.BooleanField(default=False)


class Date(models.Model):
    date = DateTimeField (auto_now=True)


class Partida(models.Model):
    puntaje_maximo= models.IntegerField(blank=True, null=True)
    puntaje_juego= models.IntegerField(blank=True, null=True)
    victoria= models.BooleanField(default=False)

    id_date = models.ForeignKey('date', models.DO_NOTHING, db_column='id_date', blank=True, null=True) #Usar now
    
    id_usuario = models.ForeignKey('usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    
    id_categoria = models.ForeignKey('categoria', models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    id_dificultad = models.ForeignKey('dificultad', models.DO_NOTHING, db_column='id_dificultad', blank=True, default=2) 
    #ID 2 es normal en dificultad
   

class Categoria(models.Model):
    categoria= models.CharField(max_length=100, blank=True, null=True)
    id_quiz = models.ForeignKey('quiz', models.DO_NOTHING, db_column='id_quiz', blank=True, null=True)


class Quiz(models.Model):
    #categoria_preg = models.CharField(max_length=100, blank=True, null=True)
    pregunta = models.CharField(max_length=200, blank=True, null=True)
    respuesta_1 = models.CharField(max_length=200, blank=True, null=True)
    respuesta_2 = models.CharField(max_length=200, blank=True, null=True)
    respuesta_3 = models.CharField(max_length=200, blank=True, null=True)
    respuesta_4 = models.CharField(max_length=200, blank=True, null=True)
    respuesta_5 = models.CharField(max_length=200, blank=True, null=True)
    correcta = models.IntegerField(default=1, blank=True, null=True)

class Dificultad(models.Model):
    vida = IntegerField()
    tiempo= IntegerField()

