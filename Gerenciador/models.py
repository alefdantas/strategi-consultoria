from django.db import models

# Create your models here.
class Personagem(models.Model):
    
    nome = models.CharField(max_length=100)

class Equipe_1(models.Model):
    nome = models.CharField(max_length=100)
class Equipe_2(models.Model):
    nome = models.CharField(max_length=100)
class Equipe_3(models.Model):
    nome = models.CharField(max_length=100)
class Equipe_4(models.Model):
    nome = models.CharField(max_length=100)
