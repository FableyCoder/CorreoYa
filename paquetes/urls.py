from django.urls import path
from paquetes import views

urlpatterns=[
    path('paquete/', views.paquetes, name="EjemplosPaquetes"),
    path('etiqueta/', views.etiqueta, name="Etiquetas")
]