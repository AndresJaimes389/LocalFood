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

def principal(request):
    return render(request, "pages/principal.html",{})

def info(request):
    titulo = "titulo dinámico"
    return render(request, "pages/info.html",{'titulo':'PQRS'})

def comunidad(request):
    titulo = "titulo dinámico"
    return render(request, "pages/comunidad.html", {'titulo':'COMUNIDAD'})

def padmin(request):
    return render(request, "pages/p_administrativo.html", {'titulo': 'Perfil Administrativo'})

def libros(request):
    return render(request, "libros/indexstock.html" , {'titulo': 'Libros'})

def crear_libro(request):
    return render(request, "libros/createstock.html", {'titulo': 'Crear Libro'})

def editar_libro(request):
    return render(request, "libros/editstock.html", {'titulo': 'Editar Libro'}) 
