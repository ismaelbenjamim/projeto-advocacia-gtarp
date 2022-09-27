from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView, FormView


class CustomLoginView(LoginView):
    template_name = 'home/login.html'


class CustomRegisterView(FormView):
    template_name = 'home/register.html'
    form_class = ''


class DiarioOficialView(TemplateView):
    template_name = 'home/diario_oficial.html'
