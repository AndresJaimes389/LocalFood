from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index),
    # path('add/',views.add_person),
    # path('show/',views.get_all_person),
    path('singin/', views.signin, name = 'signin'),
    path('singup/', views.Hola, name = 'signup'),
]