from django.urls import path
from AppCoder import views


urlpatterns = [
    path('',views.inicio,name='inicio'),
    #--------------Mascota-----------------------
    path('mascota',views.animal,name='mascota'),
    path('formularioMascota',views.formularioMascota,name='formularioMascota'),
    path('leerMascota',views.leerMascota,name='leerMascota'),
    path('busquedaMascota',views.busquedaMascota,name='busquedaMascota'),
    path('buscar/',views.buscar),
    #--------------Persona-----------------------
    #path('persona',views.persona,name='persona'),
    path('persona',views.leerPersona,name='leerPersona'),
    path('formularioPersona',views.formularioPersona,name='formularioPersona'),
    path('eliminarPersona/<persona_nombre>/',views.eliminarPersona,name='eliminarPersona'),
    path('editarPersona/<persona_nombre>/',views.editarPersona,name='editarPersona'),

     #--------------PersonaCBV-----------------------
    path('persona/list', views.PersonaList.as_view(),name='List'),
    # path(r'^(?P<pk>\d+)$', views.PersonaDetalle.as_view(),name='Detail'),
    # path(r'^nuevo$', views.PersonaCreacion.as_view(),name='New'),
    # path(r'^editar/(?P<pk>\d+)$', views.PersonaUpdate.as_view(),name='Edit'),
    # path(r'borra/(?P<pk>\d+)$', views.CursoDelete.as_view(),name='Delete'),

    #--------------Vetirinario-----------------------
    path('veterinario',views.veterinario,name='veterinario'),
    
]