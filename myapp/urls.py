from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.education, name='main'),
    path('education/', views.education, name='education'),
    path('education/<str:rubrique>/', views.education, name='education'),
    path('transport/', views.transport, name='transport'),
    path('transport/<str:rubrique>/', views.transport, name='transport'),
    path("login/", views.login_request, name="login"),
    path('logout/', views.logout_request, name='logout')
]
