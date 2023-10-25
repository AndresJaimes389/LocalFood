from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('recetas/', login_required(views.recetas, login_url = "/login/"), name = 'recetas'),

]