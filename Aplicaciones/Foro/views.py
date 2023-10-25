from django.shortcuts import render

# Create your views here.
def comunidad(request):
    titulo = "titulo dinámico"
    return render(request, "comunidad.html", {'titulo':'COMUNIDAD'})
