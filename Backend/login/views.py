from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        print('Enviando Datos')
        print(request.POST)
    elif request.method == 'GET':
        print('Obtengo Formulario')
        

    return render(request, 'signup.html', {
        'form': UserCreationForm
    })
