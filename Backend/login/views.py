from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'GET':
        print('Obtengo Formulario')
    else:
        if request.POST['password1'] == request.POST['password2']:
            # REGISTER USER
            try:
                user = User.objects.create(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('user registration successfully!')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exist'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password don\'t match'
        })
