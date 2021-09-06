from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.template import loader
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Max
from django.contrib.auth.forms import UserCreationForm
from .forms import *

from .models import *
import random

from django.contrib.auth.models import User

def registro(request):
    if request.user.is_authenticated:
        return redirect('mapa')
    else:
        form = FormCrearUsuario()
        if request.method == "POST":
            form = FormCrearUsuario(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('inicio')
        context = {'form':form}
        return render(request, 'registro.html', context)

    
def cerrarSesion(request):
    logout(request)
    return redirect('inicio')

def recuperar(request):
    template = loader.get_template('recuperar.html')
    return HttpResponse(template.render({}, request))


@login_required(login_url='inicio')
def admin(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            return redirect('mapa')
    if request.method == "POST":
        categoria = request.POST.get('categoria')
        pregunta = request.POST.get('pregunta')
        respuesta1 = request.POST.get('respuesta1')
        es_correcta_1 = request.POST.get('es_correcta_1')
        respuesta2 = request.POST.get('respuesta2')
        es_correcta_2 = request.POST.get('es_correcta_2')
        respuesta3 = request.POST.get('respuesta3')
        es_correcta_3 = request.POST.get('es_correcta_3')
        respuesta4 = request.POST.get('respuesta4')
        es_correcta_4 = request.POST.get('es_correcta_4')
        respuesta5 = request.POST.get('respuesta5')
        es_correcta_5 = request.POST.get('es_correcta_5')

        # Reconocer qué casillas están marcadas como respuestas corectas y convertirlas en booleanos:
        if es_correcta_1 != None:
            es_correcta_1 = True
        else: 
            es_correcta_1 = False

        if es_correcta_2 != None:
            es_correcta_2 = True
        else: 
            es_correcta_2 = False

        if es_correcta_3 != None:
            es_correcta_3 = True
        else: 
            es_correcta_3 = False

        if es_correcta_4 != None:
            es_correcta_4 = True
        else: 
            es_correcta_4 = False

        if es_correcta_5 != None:
            es_correcta_5 = True
        else: 
            es_correcta_5 = False

        print("Categoria:", categoria)
        print("Pregunta:", pregunta)
        print(f"Respuesta 1: {respuesta1}. Es correcta: {es_correcta_1}")
        print(f"Respuesta 2: {respuesta2}. Es correcta: {es_correcta_2}")
        print(f"Respuesta 3: {respuesta3}. Es correcta: {es_correcta_3}")
        print(f"Respuesta 4: {respuesta4}. Es correcta: {es_correcta_4}")
        print(f"Respuesta 5: {respuesta5}. Es correcta: {es_correcta_5}")

        categoria_instancia = Categoria.objects.get(id=int(categoria))

        id_list = Quiz.objects.filter().values_list('id', flat=True) #Obtiene el id mas alto de la lista de objetos
        max_id = (max(id_list)) + 1 #Suma 1 al id maximo de la lista de objetos
        quiz = Quiz(id=max_id, id_categoria=categoria_instancia, pregunta=pregunta, respuesta_1=respuesta1, correcto_1=es_correcta_1, respuesta_2=respuesta2, correcto_2=es_correcta_2, respuesta_3=respuesta3, correcto_3=es_correcta_3, respuesta_4=respuesta4, correcto_4=es_correcta_4, respuesta_5=respuesta5, correcto_5=es_correcta_5)
        print(quiz.id_categoria.id)
        quiz.save()
        print(f'{quiz} guardado!')
    preguntas = Quiz.objects.all()
    context = {'preguntas':preguntas}
    return render(request, 'admin.html', context)


@login_required(login_url='inicio')
def estadisticas(request):
    if not request.user.is_superuser:
        return redirect('mapa')
    participantes = User.objects.order_by('username') #Con order_by() ordené los objetos en orden alfabetico, pero para obtenerlos también puede usarse all()
    context = {'participantes':participantes}
    return render(request, 'estadisticas.html', context)


def inicio(request):
    if request.user.is_authenticated:
        usuario =  request.user.id
        usuario_url = str(usuario)
        return redirect('mapa/'+ usuario_url)

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
        
                login(request, user)

                usuario =  request.user.id
                
                usuario_url = str(usuario)

                return redirect('mapa/' + usuario_url)

            else:
                messages.info(request, 'Nombre de usuario o contraseña incorrectos')
                return render(request, 'inicio.html', {})

        context={}
        return render(request, 'inicio.html', context)


@login_required(login_url='inicio')
def mapa(request, id_usuario):
    usuario = request.user.id
    user_id = User.objects.get(id = 5).id
    
    if request.method == 'POST':
        print("FORM de mapa")
        form = FormPartida(request.POST) 
        form2 = FormFecha(request.POST) #Creará automáticamente fecha y hora en tabla fecha       
        
        if form.is_valid(): #Utilicé un solo if para ambos form
            form2 = form2.save(commit=False)
            form2.save()

            form = form.save(commit=False)
            form.personaje = request.POST.get('personaje')
            form.id_fecha = form2 #No se debe pasar el id así "form2.id" ya que el fk es un objeto
            form.id_usuario = request.user #Lo mismo aquí, es todo el usuario no solo el id
            dificultad = request.POST.get('dificultad') #lo mismo aquí y antes se debe obtener el objeto
            dificultad_object = Dificultad.objects.get(id=int(dificultad))
            print("Dificultad object:", dificultad)
            print("Tipo:", type(dificultad))
            form.id_dificultad =  dificultad_object
            form.puntaje_juego = 0
            if request.POST.get('dificultad') == "1":
                form.preguntas_restantes = 5
            elif request.POST.get('dificultad') == "2":
                form.preguntas_restantes = 10
            elif request.POST.get('dificultad') == "3":
                form.preguntas_restantes = 15
            print("Preguntas restante:", form.preguntas_restantes)
            form.save()

            id_part = form.id #Cada partida se guardará en tabla y contendrá datos de usuario, fecha, puntaje, etc 
            partida = Partida.objects.get(id=id_part)
            print("Preguntas restantes mapa:",partida.preguntas_restantes)
            jugada = str(id_part)
            return redirect("/juego/" + jugada)
 
    context = {
            'usuario': usuario,
            }
    return render(request, 'mapa.html', context)


@login_required(login_url='inicio')
def juego(request, id_partida):
    partida = Partida.objects.get(id=id_partida)
    print("Preguntas restantes juego:",partida.preguntas_restantes)

    #user_id = Partida.objects.get(id= 5).id
    
    #if request.method == 'POST':
    #    form = FormPartida(request.POST, instance=partida)
    #    if form.is_valid():            
    #        form.save()
            #return redirect('mapa')
    #else:
    #    form = FormPartida(instance= partida)
    print("Preguntas restantes juego fuera del POST:",partida.preguntas_restantes)

    if request.method == "POST":
        print("Se recibió POST")

        ask = request.POST
        print(ask)
        print("preguntas_restantes:",partida.preguntas_restantes)
        if "True" in ask and "False" in ask:
            print("Hubo respuestas correctas e incorrectas")
            print("- 1 punto")
        elif "True" in ask:
            print("+ 1 punto")
            partida.puntaje_juego += 1
        elif "False" in ask:
            print("- 1 punto")
            partida.puntaje_juego -= 1
        partida.preguntas_restantes -= 1
        partida.save()
        id_part = partida.id
        if partida.preguntas_restantes <= 0:
            return redirect('/victoria/'+str(id_part))
        print("preguntas_restantes tras restar:",partida.preguntas_restantes)

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
        context = { #'form': form, 
                    'respuestas': respuestas, 
                    'opciones_random': opciones_random, 
                    'pregunta_id': pregunta_id ,
                    'respuestas_random':respuestas_random, 
                    'indice_respuestas': indice_respuestas, 
                    'cantidad_respuestas': cantidad_respuestas,
                    'pregunta_random':pregunta_random,
                    'categoria': categoria, 
                    'pregunta': pregunta}

        return render(request, 'juego.html', context)
    else:
        print("No se recibió POST")

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
        context = { #'form': form, 
                    'respuestas': respuestas, 
                    'opciones_random': opciones_random, 
                    'pregunta_id': pregunta_id ,
                    'respuestas_random':respuestas_random, 
                    'indice_respuestas': indice_respuestas, 
                    'cantidad_respuestas': cantidad_respuestas,
                    'pregunta_random':pregunta_random,
                    'categoria': categoria, 
                    'pregunta': pregunta}

        return render(request, 'juego.html', context)

    

@login_required(login_url='inicio')
def ranking(request):
    context = {}
    return render(request, 'ranking.html', context)

@login_required(login_url='inicio')
def victoria(request, id_partida):
    partida = Partida.objects.get(id=id_partida)
    puntaje = partida.puntaje_juego

    context = {
        'puntaje':puntaje,
    }
    return render(request, 'victoria.html', context)

@login_required(login_url='inicio')
def derrota(request, id_partida):
    partida = Partida(id=id_partida)
    puntaje = partida.puntaje_juego

    context = {
        'puntaje':puntaje,
    }
    return render(request, 'derrota.html', context)