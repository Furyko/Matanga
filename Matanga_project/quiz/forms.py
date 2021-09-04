from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class FormCrearUsuario(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = '__all__'


class FormFecha (forms.ModelForm):
    class Meta():
        model = Fecha
        fields = '__all__'

class FormPartida (forms.ModelForm):
    class Meta():
        model = Partida
        fields = '__all__'
