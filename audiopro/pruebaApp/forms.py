from django import forms
from crispy_forms.helper import FormHelper
from pruebaApp.models import InfoContacto
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions

class FormContacto(forms.ModelForm):
    #EN INIT ES CUANDO EMPIEZO A CUSTOMIZAR EL FORM CON FORMHELPER

    class Meta:
        model = InfoContacto #ESTO ME PERMITE HEREDOR LOS CAMPOS DEL MODELO HECHO EN MODELDS
        fields = "__all__" #AQUI PERMITO QUE HEREDE TODOS LOS CAMPOS DEL MODELO


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'nombre_razon',
            'rut',
            'correo',
            'telefono',
            'comuna',
            'comentario',
            FormActions(
                Submit('enviar_cont','Enviar',css_class="btn btn-danger")
            )
        )
        