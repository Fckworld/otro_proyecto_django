from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.core import serializers
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin
from app.mixins import BaseCurrentCompany


from maintainers.models import BranchOffice
from app.filters import GenericFilter
from .forms import BranchOfficeForm, ConfirmDeleteForm
from .tables import BranchOfficeTable
from django.shortcuts import redirect
from django.views import View
from django.db.models import ProtectedError
from django.db import IntegrityError
from django.contrib import messages

# importar clase BranchOfficePDF de report.py
from maintainers.branch_office.report import BranchOfficePDF


class BranchOfficeList(BaseCurrentCompany, LoginRequiredMixin,
                        SingleTableMixin, FilterView):

    model = BranchOffice
    table_class = BranchOfficeTable
    template_name = 'maintainers/branch_office/list.html'
    filterset_class= GenericFilter
    filter_fields = ['code', 'name', 'address']
    table_pagination = {
        "per_page": 20
    }

    def get_queryset(self):
        self.filterset_class.filter_fields = self.filterset_fields
        queryset = self.model.objects.\
            filter(company = self.request.user.current_company).\
            order_by('code')

        return queryset


class BranchOfficeCreate(BaseCurrentCompany,
                        LoginRequiredMixin,
                        SuccessMessageMixin,
                        CreateView):

    form_class = BranchOfficeForm
    model = BranchOffice
    template_name = 'maintainers/branch_office/edit.html'
    success_url = reverse_lazy('maintainers:branchoffice:index')
    success_message = _('Sucursal Creada')

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(BranchOfficeCreate, self).get_form_kwargs(*args, **kwargs)
        company = self.request.user.current_company
        kwargs['company'] = company
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            obj = form.save(commit=False)
            obj.company = self.request.user.current_company
            obj.save()
            return super().form_valid(form)
        except IntegrityError:
            form.add_error("code", 'El codigo ya existe')
            response = super().form_invalid(form)
            return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class BranchOfficeEdit(BaseCurrentCompany, LoginRequiredMixin,
                        SuccessMessageMixin, UpdateView):

    model = BranchOffice
    form_class = BranchOfficeForm
    template_name = 'maintainers/branch_office/edit.html'
    success_url = reverse_lazy('maintainers:branchoffice:index')
    success_message = _("Sucursal Actualizada")

    def get_object(self, queryset=None):
        return get_object_or_404(BranchOffice, id=self.kwargs['pk'])

    @transaction.atomic
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        response = super().form_invalid(form)
        return response


class BranchOfficeDelete(BaseCurrentCompany,LoginRequiredMixin,
                        DeleteView):

    model = BranchOffice
    success_url = reverse_lazy('maintainers:branchoffice:index')
    template_name = 'maintainers/branch_office/confirm_delete.html'
    success_message = _("Sucursal Eliminada")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'form' not in kwargs:
            context['form'] = ConfirmDeleteForm()

        return context

    def post(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            form = ConfirmDeleteForm(request.POST, instance=self.object)
            if form.is_valid():
                messages.success(request, self.success_message)
                return self.delete(request, *args, **kwargs)
            else:
                return self.render_to_response(
                    self.get_context_data(form=form),
                )
        except ProtectedError:
            # Reemplazamos el error de django por una alerta
            messages.warning(request, 'Sucursal tiene datos asociados')
            return redirect(to="/maintainers/branch_office")

class BranchOfficePdfView(BaseCurrentCompany, View):
    """
    Imprimir empresa
    """
    def get(self, request, **kwargs):

        # Obtenemos empresa asociada
        current_company = request.user.current_company
        branch_office = BranchOffice.objects.filter(company=current_company)

        r = BranchOfficePDF(
            branch_office=branch_office,
            current_company=current_company
        )
        return r.pdf_response()