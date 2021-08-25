from django.contrib import admin
from .models import Quiz, Resultado, Pregunta, Respuesta

admin.site.register(Quiz)
admin.site.register(Resultado)

class RespuestasEnLinea(admin.TabularInline):
    modelo = Respuesta

class PreguntaAdmin(admin.ModelAdmin):
    enlineas = [RespuestasEnLinea]

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
