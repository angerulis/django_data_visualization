from django.urls import path
from . import views

urlpatterns = [
    path('creermodele/', views.buildmodele, name='modeleForm'),
]
