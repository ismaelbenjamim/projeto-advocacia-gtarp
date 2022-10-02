from attr import fields
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ImproperlyConfigured
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView

from projeto_advocacia.core.forms import CustomAuthenticationForm


class CustomIsAuthenticated(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomIsAuthenticated, self).dispatch(request, *args, **kwargs)


def validate_user(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/error/403/")
    else:
        return False


class ConfigView:
    raiz = None
    titulo = None
    descricao = None
    url_prefix = None

    def get_config_page(self):
        response = {
            "raiz": self.raiz,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "url_list": f'{self.url_prefix}_list',
            "url_detail": f'{self.url_prefix}_detail',
            "url_update": f'{self.url_prefix}_update',
            "url_delete": f'{self.url_prefix}_delete',
            "url_create": f'{self.url_prefix}_create',
        }
        return response


class CustomListView(ListView, ConfigView):
    filters_form = None
    fields = None

    def get_context_data(self, **kwargs):
        context = super(CustomListView, self).get_context_data(**kwargs)
        context['config'] = self.get_config_page()
        context['fields'] = self.get_fields_list()
        context['filters'] = self.get_filters()
        return context

    def get_filters(self):
        form: forms.Form = self.filters_form(self.request.GET)
        return form

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomListView, self).dispatch(request, *args, **kwargs)

    def get_fields_list(self):
        field_list = list(self.model._meta.get_fields())
        for field in field_list:
            if self.fields == '__all__':
                if not hasattr(self.model, field.name):
                    field_list.pop(field_list.index(field))
            if field.name not in self.fields:
                field_list.pop(field_list.index(field))
        return field_list


class CustomDetailView(DetailView, ConfigView):
    fields = None

    def get_context_data(self, **kwargs):
        context = super(CustomDetailView, self).get_context_data(**kwargs)
        context['config'] = self.get_config_page()
        context['fields'] = self.get_object_fields()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomDetailView, self).dispatch(request, *args, **kwargs)

    def get_object_fields(self):
        response = {self.object._meta.get_field(field): getattr(self.object, field) for field in self.fields}
        return response


class CustomCreateView(CreateView, ConfigView):
    def get_context_data(self, **kwargs):
        context = super(CustomCreateView, self).get_context_data(**kwargs)
        context['config'] = self.get_config_page()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomCreateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        self.success_url = reverse_lazy(self.get_config_page().get('url_list'))
        return super().get_success_url()


class CustomUpdateView(UpdateView, ConfigView):
    def get_context_data(self, **kwargs):
        context = super(CustomUpdateView, self).get_context_data(**kwargs)
        context['config'] = self.get_config_page()
        return context

    def get_success_url(self):
        self.success_url = reverse_lazy(self.get_config_page().get('url_detail'), kwargs={"pk": self.object.pk})
        return super().get_success_url()

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomUpdateView, self).dispatch(request, *args, **kwargs)


class CustomDeleteView(DeleteView, ConfigView):
    fields = None

    def get_context_data(self, **kwargs):
        context = super(CustomDeleteView, self).get_context_data(**kwargs)
        context['config'] = self.get_config_page()
        context['fields'] = self.get_object_fields()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomDeleteView, self).dispatch(request, *args, **kwargs)

    def get_object_fields(self):
        if self.fields == '__all__':
            self.fields = list(self.model._meta.get_fields())
            for field in self.fields.copy():
                if not hasattr(self.model, field.name):
                    self.fields.pop(self.fields.index(field))
        response = {field: getattr(self.object, field.name) for field in self.fields}
        return response

    def get_success_url(self):
        self.success_url = reverse_lazy(self.get_config_page().get('url_list'))
        return super().get_success_url()


