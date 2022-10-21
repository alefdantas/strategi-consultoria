
from django.urls import path
from .views import salva_herois,seleciona_personagem,lista_candidatos

urlpatterns = [
    path('',salva_herois,name="salva_herois"),
    path('candidatos/<str:nome>/',seleciona_personagem,name="seleciona_personagem"),
    path('lista-candidatos/',lista_candidatos,name="lista_candidatos"),
]
