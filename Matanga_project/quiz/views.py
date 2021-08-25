from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Quiz
from django.views.generic import ListView

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

def juego(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    #template = loader.get_template('juego.html')
    #return HttpResponse(template.render({}, request))
    return render(request, 'juego.html', {'obj': quiz})

def mapa(request):
    quiz = Quiz.objects.all()
    return render(request, 'mapa.html', {'obj': quiz})

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
    template = loader.get_template('registro.html')
    return HttpResponse(template.render({}, request))   

def victoria(request):
    #return HttpResponse("You're at the quiz index.")
    template = loader.get_template('victoria.html')
    return HttpResponse(template.render({}, request)) 


