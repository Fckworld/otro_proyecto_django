from curses import wrapper
from dataclasses import field
from django import forms
from pruebaApp.models import Presentation
from crispy_forms.helper import FormHelper
from pruebaApp.models import InfoContacto
from crispy_forms.layout import Submit, Layout, HTML, Field
from crispy_forms.bootstrap import FormActions

class FormContacto(forms.ModelForm):
    #EN INIT ES CUANDO EMPIEZO A CUSTOMIZAR EL FORM CON FORMHELPER
    class Meta:
        model = InfoContacto #ESTO ME PERMITE HEREDOR LOS CAMPOS DEL MODELO HECHO EN MODELDS
        fields = ['nombre_razon','rut','correo','telefono','comuna','comentario'] #AQUI PERMITO QUE HEREDE TODOS LOS CAMPOS DEL MODELO
        
        #ESTA MIERDE MUESTRA EL FORM Y QUE CAMPOS QUIERO MOSTRAR, PERO MEJOR LO HAGO EN VIEWS
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
         
            
        )
        for field in self.Meta().fields:
            self.helper.layout.append(
                Field(field, wrapper_class='row mx-auto px-5')
            )
        
        self.helper.layout.append(Submit('submit','Guardar',css_class='btn-success'))
        

class FormPresentation(forms.ModelForm):
    #EN INIT ES CUANDO EMPIEZO A CUSTOMIZAR EL FORM CON FORMHELPER

    class Meta:
        model = Presentation #ESTO ME PERMITE HEREDOR LOS CAMPOS DEL MODELO HECHO EN MODELDS
        fields = "__all__" #AQUI PERMITO QUE HEREDE TODOS LOS CAMPOS DEL MODELO
        
        #ESTA MIERDE MUESTRA EL FORM Y QUE CAMPOS QUIERO MOSTRAR, PERO MEJOR LO HAGO EN VIEWS
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            FormActions(
               
            )
        )



