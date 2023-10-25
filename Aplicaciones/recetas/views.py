from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Receta

# Create your views here.
def recetas(request):
    titulo = "titulo dinámico"
    if request.method == "GET":
        mis_recetas = Receta.objects.all()
        return render(request, "recetas.html",{'titulo':'RECETAS',
                                               "r_recetas": mis_recetas})
    else:
        if request.POST["receta"] == "":
            mis_recetas = Receta.objects.all()
            return render(request, "recetas.html",{'titulo':'RECETAS',
                                               "r_recetas": mis_recetas})
            
        else:
            print(request.POST["receta"])
            ingre_p = request.POST["receta"]
            mis_recetas = Receta.objects.filter(Ingrediente_principal__iexact = ingre_p)
            return render(request, "recetas.html",{'titulo':'RECETAS',
                                                "busqueda": "elementos encontrados",
                                                "r_recetas": mis_recetas})
            
        
