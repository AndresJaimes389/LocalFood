from django.shortcuts import render
from .models import Temporada
import calendar 

def productos(request):
    titulo = "titulo dinámico"
    meses = list(calendar.month_name)[1:]  # Obtener los nombres de los meses de enero a diciembre
    return render(request, "productos.html", {'titulo': 'Productos Temporada', 'meses': meses})


def meses(request,x):
    pro_mes= Temporada.objects.filter(mes=x)

    return render(request, "meses.html", {'titulo':'Meses','pro':pro_mes})