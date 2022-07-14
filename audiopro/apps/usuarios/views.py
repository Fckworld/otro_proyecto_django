from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm


from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, Column, Div, Field,
                                Hidden, Layout, MultiField,
                                Row, Fieldset, Submit)

class CrearCuenta(CreateView):
    template_name = 'singin.html'
    form_class = UserCreationForm()
    

    