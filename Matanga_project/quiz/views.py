from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from .forms import FormCrearUsuario

def registro(request):
    #return HttpResponse("You're at the quiz index.")
    #template = loader.get_template('registro.html')
    #return HttpResponse(template.render({}, request))
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
    #template = loader.get_template('inicio.html')
    #return HttpResponse(template.render({}, request))
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
    logout(request)
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
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('juego.html')
    return HttpResponse(template.render({}, request))

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
