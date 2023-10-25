from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import inventario
from .forms import LibroForm

def padmin(request):
    return render(request, "pages/p_administrativo.html", {'titulo': 'Perfil Administrativo'})

def libros(request):
    libros = inventario.objects.all()
    print (libros)
    return render(request, "pages/indexstock.html" , {'libros': libros})

def crear_libro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect(libros)
    return render(request, "pages/createstock.html", {'formulario': formulario})

def editar_libro(request, id):
    libro = inventario.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect(libros)
    return render(request, "pages/editstock.html", {'formulario': formulario}) 

def eliminar_libro(request, id):
    libro = inventario.objects.get(id=id).delete()
    return redirect(libros)
