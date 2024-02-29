from django.shortcuts import render
from django.views.generic import DetailView
from .models import Pet

# Create your views here.
class PetDetailView(DetailView):
    model = Pet
    template_name = "petapp/detail.html"
    context_object_name = 'pet'
