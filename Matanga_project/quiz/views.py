from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import random

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
            return redirect('inicio')
    if Categoria.objects.all().count() != 7:
        print("No se encontraron todas las categorias")
        print("Creando categorías")
        categoria_cultura = Categoria(categoria="CULTURA Y ARTE")
        categoria_cultura.save()
        categoria_historia = Categoria(categoria="HISTORIA")
        categoria_historia.save()
        categoria_deporte = Categoria(categoria="DEPORTE")
        categoria_deporte.save()
        categoria_geografia = Categoria(categoria="GEOGRAFÍA")
        categoria_geografia.save()
        categoria_economia = Categoria(categoria="ECONOMÍA")
        categoria_economia.save()
        categoria_educacion = Categoria(categoria="CIENCIA Y EDUCACIÓN")
        categoria_educacion.save()
        categoria_entretenimiento = Categoria(categoria="ENTRETENIMIENTO")
        categoria_entretenimiento.save()
        print("Categorías creadas")
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
        try:
            max_id = (max(id_list)) + 1 #Suma 1 al id maximo de la lista de objetos
        except:
            max_id = 1 #Si la tabla está vacia, no podrá realizar el max(). En ese caso, el id maximo es 1
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
    try:
        if Dificultad.objects.get(id=1).informacion == "FACIL":
            pass
    except:
        print("Dificultad facil no encontrada")
        dificultad_facil_object = Dificultad(informacion="FACIL", vida=5, tiempo=30, cant_respuestas=5)
        dificultad_facil_object.save()
        print("Dificultad facil creada")
    try:
        if Dificultad.objects.get(id=2).informacion == "NORMAL":
            pass
    except:
        print("Dificultad normal no encontrada")
        dificultad_normal_object = Dificultad(informacion="NORMAL", vida=3, tiempo=15, cant_respuestas=10)
        dificultad_normal_object.save()
        print("Dificultad nomal creada")
    try:
        if Dificultad.objects.get(id=3).informacion == "DIFICIL":
            pass
    except:
        print("Dificultad dificil no encontrada")
        dificultad_dificil_object = Dificultad(informacion="DIFICIL", vida=1, tiempo=10, cant_respuestas=15)
        dificultad_dificil_object.save()
        print("Dificultad dificil creada")
    usuario = request.user.id
    if request.method == 'POST':
        print("FORM de mapa")
        form = FormPartida(request.POST) 
        form2 = FormFecha(request.POST) #Creará automáticamente fecha y hora en tabla fecha
        if form.is_valid(): #Utilicé un solo if para ambos form
            print("Forma valida")
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
            form.puntaje_maximo = 0
            if request.POST.get('dificultad') == "1":
                form.preguntas_restantes = 5
            elif request.POST.get('dificultad') == "2":
                form.preguntas_restantes = 10
            elif request.POST.get('dificultad') == "3":
                form.preguntas_restantes = 15
            print("Preguntas restantes:", form.preguntas_restantes)
            form.id_usuario = User(id=1) #Tras encontrar el error, esto debe ser reemplazado
            form.save()
            id_part = form.id #Cada partida se guardará en tabla y contendrá datos de usuario, fecha, puntaje, etc 
            jugada = str(id_part)
            return redirect("/juego/" + jugada)
        else:
            print("Forma no valida")
            print("Error:", form.errors)
    context = {
            'usuario': usuario,
            }
    return render(request, 'mapa.html', context)

@login_required(login_url='inicio')
def juego(request, id_partida):
    partida = Partida.objects.get(id=id_partida)
    if request.method == "POST":
        print("Se recibió POST")
        ask = request.POST
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
        id_usuario = request.user.id
        if partida.preguntas_restantes <= 0:
            user = User.objects.get(pk=id_usuario)
            if partida.puntaje_juego > user.usuario.puntaje_maximo: #Si el puntaje del jugador es mayor al puntaje maximo, actualiza el puntaje maximo.
                partida.puntaje_maximo = partida.puntaje_juego
                user.usuario.puntaje_maximo = partida.puntaje_juego
                user.save()
            return redirect('/victoria/'+str(id_part))
        preguntas_rest = partida.preguntas_restantes -1
        puntaje = partida.puntaje_juego
        # SELECCIÓN CATEGORÍA
        pregunta = Quiz.objects.all().count()
        try:
            pregunta_random = random.choice(range(pregunta))
        except:
            print("No se encontaron preguntas en la base de datos.")
            return redirect('/error/')
        pregunta_base = Quiz.objects.get(id=pregunta_random + 1)
        categoria = pregunta_base.id_categoria
        pregunta_elegida = pregunta_base #PARA PASAR INDEX RESTAR 1
        pregunta = pregunta_elegida.pregunta
        pregunta_id = pregunta_elegida.id
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
        cantidad_respuestas = dificultades.get(id=1).cant_respuestas
        #DIFICULTAD NORMAL
        #cantidad_respuestas = dificultades.get(id=2).cant_respuestas
        #DIFICULTAD DIFÍCIL
        #cantidad_respuestas = dificultades.get(id=3).cant_respuestas
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
        preguntas_rest = partida.preguntas_restantes -1
        puntaje = partida.puntaje_juego
        context = { #'form': form, 
                    'respuestas': respuestas,
                    'opciones_random': opciones_random,
                    'pregunta_id': pregunta_id,
                    'respuestas_random':respuestas_random,
                    'indice_respuestas': indice_respuestas,
                    'cantidad_respuestas': cantidad_respuestas,
                    'pregunta_random':pregunta_random,
                    'categoria': categoria,
                    'pregunta': pregunta,
                    'preguntas_rest':preguntas_rest,
                    'puntaje':puntaje,
                    }
        return render(request, 'juego.html', context)
    else:
        print("No se recibió POST")
        pregunta = Quiz.objects.all().count()
        try:
            pregunta_random = random.choice(range(pregunta))
        except:
            print("No se añadieron preguntas aún.")
            return redirect('/error/')
        pregunta_base = Quiz.objects.get(id=pregunta_random + 1)
        categoria = pregunta_base.id_categoria
        pregunta_elegida = pregunta_base #PARA PASAR INDEX RESTAR 1
        pregunta = pregunta_elegida.pregunta
        pregunta_id = pregunta_elegida.id
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
        cantidad_respuestas = dificultades.get(id=1).cant_respuestas
        #DIFICULTAD NORMAL
        #cantidad_respuestas = dificultades.get(id=2).cant_respuestas
        #DIFICULTAD DIFÍCIL
        #cantidad_respuestas = dificultades.get(id=3).cant_respuestas
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
        preguntas_rest = partida.preguntas_restantes -1
        puntaje = partida.puntaje_juego
        context = { #'form': form,
                    'respuestas': respuestas,
                    'opciones_random': opciones_random,
                    'pregunta_id': pregunta_id,
                    'respuestas_random':respuestas_random,
                    'indice_respuestas': indice_respuestas,
                    'cantidad_respuestas': cantidad_respuestas,
                    'pregunta_random':pregunta_random,
                    'categoria': categoria,
                    'pregunta': pregunta,
                    'preguntas_rest':preguntas_rest,
                    'puntaje':puntaje,
                    }
        return render(request, 'juego.html', context)

@login_required(login_url='inicio')
def ranking(request):
    usuarios = Usuario.objects.all().order_by("-puntaje_maximo")
    print("usuarios: ", usuarios)
    context = {
        "usuarios": usuarios
    }
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

@login_required(login_url='inicio')
def error(request):
    context = {
        "mensaje": "El administrador del sitio todavía no a cargado preguntas ni respuestas."
    }
    return render(request, 'error.html', context)