import django
from django.http import HttpResponse
from django.template import Template, Context #LIBRERIAS PARA USAR PLANTILLAS INDEX.HTML
#ESTA SERIA LA MALA FORMA DE IMPORTAR UNA PLANTILLA
#html_externo = open("C:/Users/seba_/Documents/DUOC/Estudio_y_Proyectos/otro_proyecto_django/audiopro/audiopro/templates/index.html")
#    plt = Template(html_externo.read())
#    html_externo.close()
#    contexto = Context()
#    pagina = plt.render(contexto)
#    return HttpResponse(pagina)
from django.template import loader
#modulo para usar metodo get_template
#TENGO QUE IR A SETTINGS PARA DECIRLE A DJANGO DONDE TIENE QUE CARGAR LAS PLANTILLAS
from django.shortcuts import render

def index(request):
    #RENDER NECESITA 3 PARAMETROS, REQUEST, DIRECCION TEMPLATE, Y EL CONTEXTO QUE ES OPCIONAL
    return render(request,'index.html')

def hija(request):
    return render(request,'hija.html')
