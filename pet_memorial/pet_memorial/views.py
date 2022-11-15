from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic import View

class Home(TemplateView):
    template_name = 'home.html'
