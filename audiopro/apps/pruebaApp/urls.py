from django.urls import path

from apps.pruebaApp.views import *
app_name= 'pruebaApp'
#APP_NAME ME SIRVE PARA PODER UTILIZAR EL REVERSE_LAZY, DICIENDOLE QUE APP VAMOS A USAR Y EL NOMBRE (name='contacto_url')
#DE LA URL A LA  QUE VAMOS REDIRECCIONAR
urlpatterns = [
    #PRIMER PARAMETRO PARA EL DIRECCIONAR CON URL, Y EL SEGUNDO ES EL NOMBRE DE LA FUNCION 
    #QUE ESTA EN LAS VISTAS (NO OLVIDAR IMPORTARLAS).
    path('',Inicio.as_view(),name='inicio_url'),
    path('productos/',MostrarProductos.as_view(), name='productos_url'),
    path('lista/',IndexView.as_view(),name="formulario_url"),
    path('detallito/<int:pk>',DetalleContacto.as_view(),name='detallito_url'),
    path('contacto/',CrearContacto.as_view(),name='contacto_url'),
    path('actualizar/<int:pk>',ActualizarContacto.as_view(),name='actualizar_url')

]