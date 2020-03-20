from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
# from .models import Student, Year_Of_Reg, Book

# Create your views here.

class HomeView(TemplateView):
    template_name = 'scanner\index.html'