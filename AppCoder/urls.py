from django.urls import path
from AppCoder import views


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('mascota',views.animal,name='mascota'),
    path('persona',views.persona,name='persona'),
    path('veterinario',views.veterinario,name='veterinario'),
    path('formularioMascota',views.formularioMascota,name='formularioMascota'),
    path('busquedaMascota',views.busquedaMascota,name='busquedaMascota'),
    path('buscar/',views.buscar),
]