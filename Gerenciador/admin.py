from django.contrib import admin

from .models import  Equipe_1, Equipe_2, Equipe_3, Equipe_4, Personagem

# Register your models here.
admin.site.register(Personagem)
admin.site.register(Equipe_1)
admin.site.register(Equipe_2)
admin.site.register(Equipe_3)
admin.site.register(Equipe_4)

