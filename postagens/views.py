from django.shortcuts import render
from django.views.generic import ListView
from .models import Postagem


class HomePageView(ListView):
    model = Postagem
    template_name = 'home.html'

