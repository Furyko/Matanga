from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from .forms import FormCrearUsuario

from .models import *
import random

def registro(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('registro.html')
    return HttpResponse(template.render({}, request))
   
    if request.user.is_authenticated:
        return redirect('mapa')
    else:
        form = FormCrearUsuario()
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('inicio')
        context = {'form':form}
        return render(request, 'registro.html', context)
        

def inicio(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render({}, request))
    
    if request.user.is_authenticated:
        return redirect('mapa')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('mapa')
            else:
                messages.info(request, 'Nombre de usuario o contraseña incorrectos')
                return render(request, 'inicio.html', {})

        context = {}
        return render(request, 'inicio.html', context)
    

def cerrarSesion(request):
    #logout(request)
    return redirect('inicio')

def recuperar(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('recuperar.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='inicio')
def admin(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('admin.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='inicio')
def fin(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('fin.html')
    return HttpResponse(template.render({}, request))


@login_required(login_url='inicio')
def juego(request):
    categorias = Categoria.objects.all()

    # SELECCIÓN CATEGORÍA
    #random básico
    cantidad_cat = Categoria.objects.all().count() 
    ubicacion_index = random.choice(range(cantidad_cat)) 

    #Id categoria != index de categoría -> se corrige
    ubicacion_cat_id = ubicacion_index +1

    #Para CONTEXTO la cat segun su ID - No habrá problemas si se agrega una nueva cat luego
    categoria = categorias.get(id=ubicacion_cat_id).categoria 
    

    # SELECCION PREGUNTAS de la CATEGORÍA RANDOM
    quiz = Quiz.objects.all()
    preguntas_cat = [] #Se guardan los id de toda pregunta de esa categoria
    cada_quiz_id_cat = []
    categorias_coincidentes = []
    
    for cada_quiz in quiz:
        #Iguala el id de categoría elegida al azar con la de lista de quiz
        if cada_quiz.id_categoria.id == ubicacion_cat_id:
            cada_quiz_id_cat.append(cada_quiz.id)
            #Lista de id que tienen la misma categoría dentro de quiz
            preguntas_cat.append(cada_quiz.id)
            categorias_coincidentes.append(cada_quiz.id_categoria.id)
          
    #Random de id de la misma categoria, y se guarda en pregunta
    pregunta_random = random.choice(preguntas_cat)
    pregunta_elegida = quiz[pregunta_random - 1] #PARA PASAR INDEX RESTAR 1 
    pregunta = pregunta_elegida.pregunta
    pregunta_id = pregunta_elegida.id
    categoria_pregunta = pregunta_elegida.id_categoria.id
 

    #GET RESPUESTAS de la PREGUNTA de la CATEGORÍA RANDOM
    dificultades = Dificultad.objects.all()

    respuestas_totales_ord = [pregunta_elegida.respuesta_1, 
                        pregunta_elegida.respuesta_2,
                        pregunta_elegida.respuesta_3,
                        pregunta_elegida.respuesta_4,
                        pregunta_elegida.respuesta_5]
    
    # index de las respuestas ordenadas coninciden con el index del bool de correcto
    opciones_totales_ord = [pregunta_elegida.correcto_1,
                        pregunta_elegida.correcto_2,
                        pregunta_elegida.correcto_3,
                        pregunta_elegida.correcto_4,
                        pregunta_elegida.correcto_5]
    
    ordinales = ['a)', 'b)', 'c)', 'd)', 'e)']
    
    #EN GENERACIÓN DE PARTIDAS SE DEBERÁ HACER UN IF AQUÍ

    #DIFICULTAD FÁCIL
    #cantidad_respuestas = dificultades.get(id=1).cant_respuestas

    #DIFICULTAD NORMAL
    #cantidad_respuestas = dificultades.get(id=2).cant_respuestas
    

    #DIFICULTAD DIFÍCIL
    cantidad_respuestas = dificultades.get(id=3).cant_respuestas
    
    # ordinales según dificultad
    ordinales_dificil = ordinales[0:cantidad_respuestas]
    
    # generar respuestas aleatorias según cantidad dificultad
    indice_respuestas = random.sample(range(0,cantidad_respuestas), cantidad_respuestas) 

    respuestas_random = []
    for indice in indice_respuestas:
        respuestas_random.append(respuestas_totales_ord[indice])
    
    opciones_random = []
    for indice in indice_respuestas:
        opciones_random.append(opciones_totales_ord[indice])
    
    respuestas = {} #Por último se sumará todo a un solo diccionario para usar en html
    for indice in range(cantidad_respuestas):
        respuestas[indice] = (ordinales_dificil[indice], respuestas_random[indice], opciones_random[indice])

    #Eliminar a lo ultimo lo q no sirve de contexto
    context = {'respuestas': respuestas, 'opciones_random': opciones_random, 'pregunta_id': pregunta_id ,'respuestas_random':respuestas_random, 'indice_respuestas': indice_respuestas, 'cantidad_respuestas': cantidad_respuestas,'pregunta_random':pregunta_random,'categoria': categoria, 'pregunta': pregunta}
    return render(request, 'juego.html', context) 
    
'''
    request.method == 'POST':
        form = Corregir3ro_1ra_punto1(request.POST, instance=ejercicio)



    context = {'form': form, 'punto': ejercicios}
    return render(request, 'estudiantes/corregir_ejercicio.html', context)              
'''
    #template = loader.get_template('juego.html')
    #return HttpResponse(template.render({}, request))


@login_required(login_url='inicio')
def mapa(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('mapa.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='inicio')
def ranking(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('ranking.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='inicio')
def victoria(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('victoria.html')
    return HttpResponse(template.render({}, request)) 
