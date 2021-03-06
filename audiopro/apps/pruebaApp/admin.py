from django.contrib import admin
#AQUI REGISTRARE LAS CLASES CREADAS EN MODELS.PY PARA PODER MANIPULARLOS
#DESDE EL PANEL DE CONTROL ADMIN DE DJANGO.
from apps.pruebaApp.models import Cliente, Producto, Pedido, InfoContacto, Speaker, Track, Presentation
#AQUI REGISTRARE LAS CLASES CREADAS EN MODELS.PY PARA POD

class ClientesAdmin(admin.ModelAdmin):
    #EL LIST_DISPLAY PREDOMINA SOBRE LA FUNCION CONSTRUCTOR DEL MODELO
    list_display=('nombre','direccion','telefono') #EL NOMBRE DE ESTA VARIABLE TIENE QUE SER TAL CUAL
    search_fields = ('nombre','telefono')

class ProductosAdmin(admin.ModelAdmin):
    list_display=('id','nombre','seccion','precio')
    list_filter = ('seccion',)

class PedidosAdmin(admin.ModelAdmin):
    list_display=('id','numero','fecha','entregado')
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'

class InfoContactoAdmin(admin.ModelAdmin):
    list_display=('id','nombre_razon','correo','telefono','comuna')

class SpeakerAdmin(admin.ModelAdmin):
    list_display=('name',)
class TrackAdmin(admin.ModelAdmin):
    list_display=('title',)

class PresentationAdmin(admin.ModelAdmin):
    list_display= ('title','abstract', 'track','speaker')

admin.site.register(InfoContacto,InfoContactoAdmin)

admin.site.register(Cliente,ClientesAdmin)#LADO IZQUIERDO: NOMBRE DE LA CLASE QUE VOY A DESPLEGAR, LADO DERECHO: COMO VOY A DESPLEGARLO
admin.site.register(Producto,ProductosAdmin )
admin.site.register(Pedido,PedidosAdmin)

admin.site.register(Speaker,SpeakerAdmin)
admin.site.register(Track,TrackAdmin)
admin.site.register(Presentation,PresentationAdmin)