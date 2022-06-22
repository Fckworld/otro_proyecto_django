#from django.http import HttpResponse
#from django.template import Template, Context #LIBRERIAS PARA USAR PLANTILLAS INDEX.HTML
#ESTA SERIA LA MALA FORMA DE IMPORTAR UNA PLANTILLA
#html_externo = open("C:/Users/seba_/Documents/DUOC/Estudio_y_Proyectos/otro_proyecto_django/audiopro/audiopro/templates/index.html")
#    plt = Template(html_externo.read())
#    html_externo.close()
#    contexto = Context()
#    pagina = plt.render(contexto)
#    return HttpResponse(pagina)
#from django.template import loader
#modulo para usar metodo get_template
#TENGO QUE IR A SETTINGS PARA DECIRLE A DJANGO DONDE TIENE QUE CARGAR LAS PLANTILLAS
from dataclasses import field
from pyexpat import model
from django.shortcuts import render
from pruebaApp.models import Presentation
from pruebaApp.forms import FormContacto
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, Column, Div, Field,
                                Hidden, Layout, MultiField,
                                Row, Fieldset, Submit)

class IndexView(ListView):
    model= Presentation
    context_object_name='formulario'
    template_name= 'lista_form.html'
    
    queryset= Presentation.objects.all()


class CrearContacto(CreateView,SuccessMessageMixin):
    form_class= FormContacto
    template_name='contacto.html'
    success_url= reverse_lazy('pruebaApp:formulario_url')
    success_message= 'GUARDADO COMPLETADO'


class DetalleContacto(DetailView):
    context_object_name = 'detallito'
    model = Presentation
    template_name = 'detallito.html'

class Inicio(TemplateView):
    template_name='inicio.html'
""" 
def inicio(request):
    #RENDER NECESITA 3 PARAMETROS, REQUEST, DIRECCION TEMPLATE, Y EL CONTEXTO QUE ES OPCIONAL
    return render(request,'inicio.html')
 
def hija(request):
    return render(request,'hija.html')
"""
def muestra_productos(request):
    return render(request,'muestra_productos.html')

def contactotest(request):
    if request.method=="POST":
        miForm = FormContacto(request.POST)

        if miForm.is_valid():
            dataForm = miForm.cleaned_data
            return render(request,"gracias.html")
    else:
        miForm = FormContacto()
    
    datos = {
        'formi':miForm,
        'variable':'informacion de variable',
    }

    return render(request,"info_form.html",datos)



