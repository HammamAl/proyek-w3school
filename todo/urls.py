from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('anggota/', views.home, name='home'),
    path('details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing')
]

