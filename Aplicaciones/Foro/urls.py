from django.urls import path
from . import views


urlpatterns = [
    path('comunidad/', views.comunidad, name = 'comunidad'),

]