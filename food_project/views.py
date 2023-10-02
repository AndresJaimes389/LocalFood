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
