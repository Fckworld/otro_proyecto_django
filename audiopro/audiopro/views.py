import django
from django.http import HttpResponse
from django.template import Template, Context #LIBRERIAS PARA USAR PLANTILLAS INDEX.HTML

def index(request):
    html_externo = open("C:/Users/seba_/Documents/DUOC/Estudio_y_Proyectos/otro_proyecto_django/audiopro/audiopro/templates/index.html")
    plt = Template(html_externo.read())
    html_externo.close()
    contexto = Context()
    pagina = plt.render(contexto)
    return HttpResponse(pagina)
