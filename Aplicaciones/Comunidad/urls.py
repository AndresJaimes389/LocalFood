from django.urls import path
from . import views


urlpatterns = [
    path('comunidad/', views.create_thread, name = 'create_thread'),

]