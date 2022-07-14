# -- encoding: utf-8 --

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, Column, Div, Field,
                                Hidden, Layout, MultiField,
                                Row, Submit, Fieldset)
from django import forms
from django.forms import widgets
from django.urls import reverse
from django.utils.translation import gettext as _

from maintainers.models import Company, CostCenter
from app.functions import get_code_model

class ConfirmDeleteForm(forms.ModelForm):
    """
    Confirmacion eliminacion centro de costos
    """
    class Meta:
        model = CostCenter
        fields = []

    def _init_(self, *args, **kwargs):

        super()._init_(*args, **kwargs)

        url_costcenter = reverse('maintainers:costcenter:index')

        self.helper = FormHelper()
        self.helper.form_class = 'form-parsley'
        self.helper.layout = Layout(
            Div(
                Row(
                    HTML(
                        '<a class="btn btn-lg btn-warning"'
                        ' href="' + url_costcenter + '">'+_('Cancelar')+'</a>'
                    ),
                    Submit(
                            'submit','Confirmar',
                        css_class='btn btn-primary btn-lg float-right'),
                    css_class="d-flex justify-content-end"
                )
            ),
        )

class CostCenterForm(forms.ModelForm):

    class Media:
        js = (
            'parsley/parsley.min.js',
            'parsley/i18n/es.js',
            'parsley/custom_validators.js',
            'forms/form_validators.js',
        )

        css = {
            'all': ('parsley/parsley.css',)
        }

    class Meta:
        model = CostCenter
        fields = [
            'code',
            'description'
        ]
        widgets = {
            'code': forms.TextInput(),
            'description':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'required': 'required',
                    'maxlength': '30'
                }
            )
        }

    def _init_(self, *args, **kwargs):

        company = kwargs.pop('company', None)
        super(CostCenterForm, self)._init_(*args, **kwargs)

        submit_text = "Actualizar" if self.instance.pk else "Guardar"
        url_costcenter = reverse('maintainers:costcenter:index')

        self.helper = FormHelper()

        if self.instance.pk:
            self.fields['code'].widget.attrs.update({
                'class': 'form-control',
                'readonly':'readonly',
            })
        else:
            self.fields['code'].widget.attrs.update({
                'class': 'form-control',
                'required': 'required',
                'onkeypress': 'return onlyNumberKey(event)'
            })

        self.fields['code'].initial = get_code_model(CostCenter, company)
        self.helper.include_media = False
        self.helper.form_class = 'form-parsley'
        self.helper.layout = Layout(
            Div(
                Row(
                    Column('code', css_class='col-md-2'),
                    Column('description', css_class='col-md-8'),
                    css_class="justify-content-md-center"
                ),
                Div(
                    Column('bton', css_class='pt-3'),
                    Row(
                        HTML(
                            '<a class="btn btn-lg btn-warning mr-0 ml-2 my-1"'
                            ' href="' + url_costcenter + '">'+_('Cancelar')+'</a>'
                        ),
                        Submit(
                                'submit', _(f'{submit_text} Centro de Costo'),
                            css_class='btn btn-primary btn-lg float-right mr-0 ml-2 my-1'),
                        css_class="d-flex justify-content-end pr-1"
                    )
                ),
            ),
        )

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data['code']

        if self.instance.pk:
            exist = CostCenter.objects.filter(
                company=self.instance.company,
                code=code
                ).exclude(id=self.instance.pk)
            if exist.count() > 0:
                self.add_error('code','Ya existe el código')

        try:
            value_int = int(code)
        except ValueError:
            self.add_error('code', 'Código debe ser numérico')