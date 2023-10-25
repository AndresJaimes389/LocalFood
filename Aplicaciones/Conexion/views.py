from django.shortcuts import render, redirect
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation


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
                validate_password(request.POST['password1'], user=None, password_validators=password_validation.get_default_password_validators())
                
                email_validator = request.POST['email']
                if not email_validator.endswith('@gmail.com') and not email_validator.endswith('@hotmail.com') and not email_validator.endswith('@outlook.com'):
                    raise ValidationError("El correo debe ser de dominio @gmail.com, @hotmail.com o @outlok.com.")
                
                user = User.objects.create_user(
                    username = request.POST['User'], email = request.POST['email'],
                    password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio')
            except ValidationError as e:
                return render(request, "signin.html",{'titulo': 'Crear cuenta',
                                                'texto': "introduce los datos de tu cuenta o inicia sesión",
                                                'error': 'El usuario ya existe',
                                                'error': e.messages})
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
        username_or_email = request.POST.get('Username')  
        password = request.POST.get('Password')
        
        user = None
        if '@' in username_or_email:  
            user = authenticate(request, email=username_or_email, password=password)
        else:  
            user = authenticate(request, username=username_or_email, password=password)

        if user is None:
            return render(request, "login.html", {'titulo': 'Bienvenido de nuevo',
                                                  'texto': 'Inicie sesión a continuación o cree una cuenta',
                                                  'error': 'Usuario o contraseña incorrectos'})
        
        else:
            login(request, user)
            print(request.POST['Username'], request.POST['Password'])
            return redirect('inicio')
        
        
    
