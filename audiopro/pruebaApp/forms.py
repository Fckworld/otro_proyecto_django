from dataclasses import field
from django import forms
from pruebaApp.models import Presentation
from crispy_forms.helper import FormHelper
from pruebaApp.models import InfoContacto
from crispy_forms.layout import Submit, Layout, HTML, Field, Div, Column,Row
from crispy_forms.bootstrap import FormActions

class FormContacto(forms.ModelForm):
    #EN INIT ES CUANDO EMPIEZO A CUSTOMIZAR EL FORM CON FORMHELPER
    
    nombre_razon = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre o Razon'}))
    rut = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Rut'}))
    correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Correo'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono'}))
    comuna = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comuna'}))
    comentario = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comentario'}))
    class Meta:
        model = InfoContacto #ESTO ME PERMITE HEREDOR LOS CAMPOS DEL MODELO HECHO EN MODELDS
        fields = ['nombre_razon','rut','correo','telefono','comuna','comentario'] #AQUI PERMITO QUE HEREDE TODOS LOS CAMPOS DEL MODELO
        
        #ESTA MIERDE MUESTRA EL FORM Y QUE CAMPOS QUIERO MOSTRAR, PERO MEJOR LO HAGO EN VIEWS
    def __init__(self, *args, **kwargs):
        calzo = 'px-5 py-2'
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_show_labels=False
        vl =  Div(
                    Div(
                        Field('nombre_razon'),css_class='px-5 py-2 pt-4',),
                    Div(
                        Field('rut'),css_class=calzo,),
                    Div(
                        Field('correo'),css_class='px-5 py-2',),
                    Div(
                        Field('telefono'),css_class='px-5 py-2',),
                    Div(
                        Field('comuna'),css_class='px-5 py-2',),
                    Div(
                        Field('comentario'),css_class='px-5 py-2',),
                    Submit('submit','Enviar',css_class='my-5'),
                        
                    css_class='col bg-secondary mx-5 rounded',css_id='columna_form',
        )
        self.helper.layout = Layout(vl)
        
        
"""         for field in self.Meta().fields:
            self.helper.layout.append(
                Field(field, wrapper_class='row mx-auto px-5')
            )
        self.helper.layout(

        )
        self.helper.layout.append(Submit('submit','Guardar',css_class='btn-success'))
         """

class FormPresentation(forms.ModelForm):
    #EN INIT ES CUANDO EMPIEZO A CUSTOMIZAR EL FORM CON FORMHELPER

    class Meta:
        model = Presentation #ESTO ME PERMITE HEREDOR LOS CAMPOS DEL MODELO HECHO EN MODELDS
        fields = "__all__" #AQUI PERMITO QUE HEREDE TODOS LOS CAMPOS DEL MODELO
        
    class Media:
        css={'all':('/static/stylecontactoform.css'),}
        #ESTA MIERDE MUESTRA EL FORM Y QUE CAMPOS QUIERO MOSTRAR, PERO MEJOR LO HAGO EN VIEWS
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            FormActions(
               
            )
        )



