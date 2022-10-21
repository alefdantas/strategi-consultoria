
from django.urls import path
from .views import forma_equipe_1, forma_equipe_2, forma_equipe_3, forma_equipe_4, retira_equipe_1, retira_equipe_2, retira_equipe_3, retira_equipe_4, retira_heroi, salva_herois,seleciona_personagem,lista_candidatos

urlpatterns = [
    path('',salva_herois,name="salva_herois"),
    path('candidatos/<str:nome>/',seleciona_personagem,name="seleciona_personagem"),
    path('lista-candidatos/',lista_candidatos,name="lista_candidatos"),
    path('retira-heroi/<int:id>',retira_heroi,name="retira_heroi"),
    path('forma-equipe-1/<int:id>/',forma_equipe_1,name="forma_equipe_1"),
    path('retira-equipe-1/<int:id>/',retira_equipe_1,name="retira_equipe_1"),
    path('forma-equipe-2/<int:id>/',forma_equipe_2,name="forma_equipe_2"),
    path('retira-equipe-2/<int:id>/',retira_equipe_2,name="retira_equipe_2"),
    path('forma-equipe-3/<int:id>/',forma_equipe_3,name="forma_equipe_3"),
    path('retira-equipe-3/<int:id>/',retira_equipe_3,name="retira_equipe_3"),
    path('forma-equipe-4/<int:id>/',forma_equipe_4,name="forma_equipe_4"),
    path('retira-equipe-4/<int:id>/',retira_equipe_4,name="retira_equipe_4"),

]
