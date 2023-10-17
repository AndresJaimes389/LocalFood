from django.shortcuts import render
from .models import person_collection
from django.http import HttpResponse
from django.contrib.auth.models import User

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
                return HttpResponse("Usuario creado satisfactoriamente")
            except:
                return HttpResponse("El usuario ya existe")
        return HttpResponse("Las contraseñas no coinciden")    
    