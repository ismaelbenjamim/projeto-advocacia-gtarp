from attr import fields
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
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


class NotPermissionView(TemplateView):
    template_name = "error/403.html"


class NotExistsView(TemplateView):
    template_name = "error/404.html"


class CustomLoginView(LoginView):
    template_name = 'home/login.html'
    form_class = CustomAuthenticationForm


class CustomLogoutView(LogoutView):
    template_name = 'home/logout.html'


class RegisterView(FormView):
    template_name = 'home/register.html'
    form_class = ''


class DiarioOficialView(TemplateView):
    template_name = 'home/diario_oficial.html'


class ConfigView:
    raiz = None
    titulo = None
    descricao = None
    campos_tabela = None
    campos_filtro = None

    def get_config_page(self):
        response = {
            "raiz": self.raiz,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "campos_tabela": self.campos_tabela,
            "campos_filtro": self.campos_filtro,
        }
        return response


    def campos_tabela(self):
        fields = []
        for field in self.object._meta.get_fields():
            if field.name in self.fields:
                fields.append(field)
        return fields


class CustomListView(ListView, ConfigView):
    def get_context_data(self, **kwargs):
        context = super(CustomListView, self).get_context_data(**kwargs)
        context['config'] = self.get_config_page()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomListView, self).dispatch(request, *args, **kwargs)


class CustomDetailView(DetailView, ConfigView):
    def get_context_data(self, **kwargs):
        context = super(CustomDetailView, self).get_context_data(**kwargs)
        context['config'] = self.get_config_page()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomDetailView, self).dispatch(request, *args, **kwargs)


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


class CustomUpdateView(UpdateView, ConfigView):
    def get_context_data(self, **kwargs):
        context = super(CustomUpdateView, self).get_context_data(**kwargs)
        context['config'] = self.get_config_page()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomUpdateView, self).dispatch(request, *args, **kwargs)


class CustomDeleteView(DeleteView, ConfigView):

    def get_context_data(self, **kwargs):
        context = super(CustomDeleteView, self).get_context_data(**kwargs)
        context['config'] = self.get_config_page()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomDeleteView, self).dispatch(request, *args, **kwargs)

