from django.shortcuts import render
from django.views.generic.detail import DetailView
from pet.models import Pet

class PetDetailView(DetailView):
    model = Pet
    template_name = "pet_profile.html"
