from django.views.generic import TemplateView
from .models import Menu, Kategoria, Alergeny, Promocje

from django.shortcuts import render

# Create your views here.

class MainPageView(TemplateView):
    template_name = "page/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = Menu.objects.all()
        return context

class MenuPageView(TemplateView):
    template_name = "page/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = Menu.objects.all()
        context['kategorie'] = Kategoria.objects.all()
        context['alergeny'] = Alergeny.objects.all()
        context['promocje'] = Promocje.objects.all()
        return context


