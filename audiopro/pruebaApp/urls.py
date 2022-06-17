from django.urls import path

from pruebaApp.views import *
app_name= 'pruebaApp'
#APP_NAME ME SIRVE PARA PODER UTILIZAR EL REVERSE_LAZY, DICIENDOLE QUE APP VAMOS A USAR Y EL NOMBRE (name='contacto_url')
#DE LA URL A LA  QUE VAMOS REDIRECCIONAR
urlpatterns = [
    #PRIMER PARAMETRO PARA EL DIRECCIONAR CON URL, Y EL SEGUNDO ES EL NOMBRE DE LA FUNCION 
    #QUE ESTA EN LAS VISTAS (NO OLVIDAR IMPORTARLAS).
    path('',inicio),
    path('productos/',muestra_productos),
    path('contacto/',contacto,name='contacto_url'),

    path('hijaurl/', hija),
    path('busqueda/',busqueda_producto),
    path('respuesta/',respuesta_producto),
    path('contactot/',contactotest),
    path('lista/',IndexView.as_view(),name="formulario_url"),
    path('detallito/<int:pk>',DetalleContacto.as_view(),name='detallito_url'),
    path('indox/',CrearContacto.as_view(),name='indox_url'),

]