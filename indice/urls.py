from django.urls import path
from .views import inicio, mi_plantilla, numero_del_usuario, otra_vista, numero_random

urlpatterns = [     
    path('inicio/', inicio),
    path('', otra_vista),
    path('numero-random/', numero_random),
    path('dame-numero/<int:numero>', numero_del_usuario),
    path('mi-plantilla/', mi_plantilla),
]