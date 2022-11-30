from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("", views.Home.as_view(), name="home"),
    path("pet/", include('pet.urls')),
]
