from django.shortcuts import render
from .models import Pqrs
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def info(request):
    titulo = "titulo dinámico"
    
    if request.method == "GET":
        return render(request, "info.html",{'titulo':'PQRS'})
    else:
        c_name = request.POST["name"]
        c_email = request.POST["email"]
        c_phone = request.POST["phone"]
        c_message = request.POST["message"]
        objects_contacto = Pqrs(name=c_name, email=c_email, phone=c_phone, message=c_message)
        objects_contacto.save()
        send_email(c_name, c_email, c_phone, c_message)
        
        print(c_name, c_email, c_phone, c_message)
        
        return render(request, "info.html",{'titulo':'PQRS'})
    
    
def send_email(c_name, c_email, c_phone, c_message):
    subjects = 'Gracias por contactarnos'
    message = f"nombre: {c_name},\n email: {c_email},\n telefono: {c_phone}, mensaje: {c_message}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["local.food.a4@gmail.com"]
    send_mail(subjects, message, email_from, recipient_list)
    return True
    


# def email(email):
#     subject = 'Thank you for contact me'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['andresjl389@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     return True