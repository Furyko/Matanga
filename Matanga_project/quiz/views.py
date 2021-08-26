from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.forms import UserCreationForm
from .forms import FormCrearUsuario

# Create your views here.
def inicio(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render({}, request))

def admin(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('admin.html')
    return HttpResponse(template.render({}, request))

def fin(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('fin.html')
    return HttpResponse(template.render({}, request))

def juego(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('juego.html')
    return HttpResponse(template.render({}, request))

def mapa(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('mapa.html')
    return HttpResponse(template.render({}, request))

def ranking(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('ranking.html')
    return HttpResponse(template.render({}, request))

def recuperar(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('recuperar.html')
    return HttpResponse(template.render({}, request))

def registro(request):
    #return HttpResponse("You're at the quiz index.")
    #template = loader.get_template('registro.html')
    #return HttpResponse(template.render({}, request))
    form = FormCrearUsuario()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'registro.html', context)

def victoria(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('victoria.html')
    return HttpResponse(template.render({}, request)) 


