from django.shortcuts import render


def inicio(request):
    titulo = "titulo dinámico"
    return render(request, "pages/inicio.html",{'titulo': 'Inicio'})

def recetas(request):
    titulo = "titulo dinámico"
    return render(request, "pages/recetas.html",{'titulo':'RECETAS'})

def suscripcion(request):
    titulo = "titulo dinámico"
    return render(request, "pages/suscripcion.html",{'titulo':'Detalle de la suscripcion'})

def login(request):
    titulo = "titulo dinámico"
    texto = "texto dinámico"
    return render(request, "pages/login.html",{'titulo': 'Bienvenido de nuevo',
                                               'texto': 'Inicie sesión a continuación o cree una cuenta'})

def signin(request):
    titulo = "titulo dinámico"
    texto = "texto dinámico"
    return render(request, "pages/signin.html",{'titulo': 'Crear cuenta',
                                                'texto': "introduce los datos de tu cuenta o inicia sesión"})

def principal(request):
    return render(request, "pages/principal.html",{})

def info(request):
    titulo = "titulo dinámico"
    return render(request, "pages/info.html",{'titulo':'PQRS'})