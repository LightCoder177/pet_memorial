from django.contrib import admin
from django.urls import path
from . import views as pet_views
from .models import Pet

urlpatterns = [
    path('<slug:slug>', pet_views.PetDetailView.as_view(), name='pet_details'),
]
