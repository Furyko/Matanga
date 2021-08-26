from django.db import models
from django.db.models.fields import IntegerField
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
    id_partida = models.ForeignKey('partida', models.DO_NOTHING, db_column='id_partida', blank=True, null=True)



class Partida (models.Model):
    puntaje_maximo= models.IntegerField(null=True)
    puntaje_juego= models.IntegerField(null=True)
    dificultad = models.CharField(max_length=20, default="normal")
    id_categoria = models.ForeignKey('categoria', models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)



# Create your models here.
class Categoria(models.Model):
    Categoria = models.CharField(max_length=50)
    topico = models.CharField(max_length=200)
    id_pregunta = models.ForeignKey('pregunta', models.DO_NOTHING, db_column='id_pregunta', blank=True, null=True)
    

    def __str__(self):
        return f"{self.nombre}-{self.topico}"

    def obtener_preguntas(self):
        return self.definir_pregunta.all()

    class Meta:
        verbose_name_plural = 'Quizes'




class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    id_respuesta = models.ForeignKey('respuesta', models.DO_NOTHING, db_column='id_respuesta', blank=True, null=True)

    def obtener_respuestas(self):
        return self.definir_respuesta.all()

    def __str__(self):
        return str(self.texto_pregunta)




class Respuesta(models.Model):
    texto_respuesta = models.CharField(max_length=200)
    opcion_correcta = models.BooleanField(default=False)

    def __str__(self):
        return f"pregunta: {self.pregunta.texto_pregunta}, respuesta: {self.texto_respuesta}, correcta: {self.opcion_correcta}"


