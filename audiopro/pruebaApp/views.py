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
from pruebaApp.forms import FormContacto

def inicio(request):
    #RENDER NECESITA 3 PARAMETROS, REQUEST, DIRECCION TEMPLATE, Y EL CONTEXTO QUE ES OPCIONAL
    return render(request,'inicio.html')

def hija(request):
    return render(request,'hija.html')

def busqueda_producto(request):
    return render(request,'busqueda_producto.html')
def muestra_productos(request):
    return render(request,'muestra_productos.html')

def respuesta_producto(request):
    return render(request,'respuesta_producto.html')

def contacto(request):
    if request.method=="POST":
        return render(request,"gracias.html")
    return render(request,'contacto.html')

def contactotest(request):
    if request.method=="POST":
        miForm = FormContacto(request.POST)

        if miForm.is_valid():
            dataForm = miForm.cleaned_data
            return render(request,"gracias.html")
    else:
        miForm = FormContacto()

    return render(request,"info_form.html",{"formi":miForm})

