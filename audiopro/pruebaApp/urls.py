from django.urls import path

from pruebaApp import views
urlpatterns = [
    #PRIMER PARAMETRO PARA EL DIRECCIONAR CON URL, Y EL SEGUNDO ES EL NOMBRE DE LA FUNCION 
    #QUE ESTA EN LAS VISTAS (NO OLVIDAR IMPORTARLAS).
    path('',views.inicio),
    path('productos/',views.muestra_productos),
    path('contacto/',views.contacto),

    path('hijaurl/', views.hija),
    path('busqueda/', views.busqueda_producto),
    path('respuesta/', views.respuesta_producto),
    path('contactot/',views.contactotest),
    
]