from django.urls import path
from . import views

urlpatterns = [
    path('education/', views.education, name='education'),
    path('transport/', views.transport, name='transport'),
]
