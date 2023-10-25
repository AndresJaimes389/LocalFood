from django.urls import path
from . import views


urlpatterns = [
    path('padmin/', views.padmin , name = 'perfil_administrativo'),
    path('indexlibros/', views.libros, name = 'libros'),
    path('libroscrear/', views.crear_libro, name = 'crear_libros'),
    path('libroseditar/', views.editar_libro , name = 'editar_libros'),
    path('libroseditar/<int:id>', views.editar_libro , name = 'editar_libros'),
    path('eliminar/<int:id>', views.eliminar_libro, name = 'eliminar_libros'),

]