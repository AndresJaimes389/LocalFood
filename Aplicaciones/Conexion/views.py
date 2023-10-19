from django.shortcuts import render, redirect
from .models import person_collection
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

# def index(request):
#     return HttpResponse("<h1>App is running..</h1>")

# def add_person(request):
#     records = {
#         'first_name': 'Andres',
#         'last_name': 'Carrillo',
#     }
#     person_collection.insert_one(records)
#     return HttpResponse("New person added")

# def get_all_person(request):
    
#     consulta = {}
#     proyeccion = {'first_name': 'Andres'}
    
#     person = person_collection.find(consulta, proyeccion)
#     return HttpResponse(person)


def Hola(request):
    return HttpResponse("HelloWorld")

def signin(request):
    titulo = "titulo dinámico"
    texto = "texto dinámico"
    
    if request.method == 'GET':
        print("Enviando formulario")
        return render(request, "signin.html",{'titulo': 'Crear cuenta',
                                                'texto': "introduce los datos de tu cuenta o inicia sesión"})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registro
            try:
                user = User.objects.create_user(
                    username = request.POST['User'], email = request.POST['email'],
                    password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio')
            except:
                return render(request, "signin.html",{'titulo': 'Crear cuenta',
                                                'texto': "introduce los datos de tu cuenta o inicia sesión",
                                                'error': 'El usuario ya existe'})
        return render(request, "signin.html",{'titulo': 'Crear cuenta',
                                                'texto': "introduce los datos de tu cuenta o inicia sesión",
                                                'error': 'Las contraseñas no coinciden'})    
    
    
def signout(request):
    logout(request)
    return redirect("principal")


def login_view(request):
    titulo = "titulo dinámico"
    texto = "texto dinámico"
    
    if request.method == "GET":
        return render(request, "login.html",{'titulo': 'Bienvenido de nuevo',
                                                'texto': 'Inicie sesión a continuación o cree una cuenta'})
    
    else:
        # print(request.POST)
        user = authenticate(request, username=request.POST['Username'], password=request.POST['Password'])
        
        if user is None:
            return render(request, "login.html",{'titulo': 'Bienvenido de nuevo',
                                                    'texto': 'Inicie sesión a continuación o cree una cuenta',
                                                    'error': 'Usuario o contraseña incorrectos'})
        
        else:
            login(request, user)
            return redirect('inicio')
        
        
    
    