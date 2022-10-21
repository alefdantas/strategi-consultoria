from django.db import models

# Create your models here.
class Personagem(models.Model):
    
    nome = models.CharField(max_length=100)
    