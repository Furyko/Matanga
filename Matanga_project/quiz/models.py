import datetime

from django.db import models
from django.utils import timezone

DIFICULTAD_RESPUESTAS = (
    ('facil', 'facil'),
    ('intermedio', 'intermedio'),
    ('dificil', 'dificil'),
)

class Quiz(models.Model):
    nombre = models.CharField(max_length=120)
    topico = models.CharField(max_length=120)
    cantidad_de_preguntas = models.IntegerField()
    tiempo = models.IntegerField(help_text="Duracion del quiz en minutos")
    dificultad = models.CharField(max_length=10, choices=DIFICULTAD_RESPUESTAS)

    def __str__(self):
        return f"{self.nombre}-{self.topico}"[:self.cantidad_de_preguntas]

    def obtener_preguntas(self):
        return self.definir_pregunta.all()

    class Meta:
        verbose_name_plural = 'Quizes'

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def obtener_respuestas(self):
        return self.definir_respuesta.all()

    def __str__(self):
        return str(self.texto_pregunta)

class Respuesta(models.Model):
    texto_respuesta = models.CharField(max_length=200)
    opcion_correcta = models.BooleanField(default=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"pregunta: {self.pregunta.texto_pregunta}, respuesta: {self.texto_respuesta}, correcta: {self.opcion_correcta}"

class Usuario(models.Model):
    nombre= models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    cel= models.ImageField(null=True)
    clave= models.CharField(max_length=100)
    admin = models.BooleanField(default=False)

class Resultado(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntaje = models.FloatField()

    def __str__(self):
        return str(self.pk)