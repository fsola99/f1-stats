from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('circuits/', views.circuits_view, name='circuits'),
    path('constructors/', views.constructors_view, name='constructors'),
    path('drivers/', views.drivers_view, name='drivers'),
    path('standings/', views.standings_view, name='standings'),
]
