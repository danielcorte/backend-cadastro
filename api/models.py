from django.db import models


class Professores(models.Model):
    ni = models.CharField(max_length=15)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    cel = models.CharField(max_length=255)
    ocup = models.FloatField()

class Disciplinas(models.Model):
    sigla = models.CharField(max_length=8)
    nome = models.CharField(max_length=255)
    semestre = models.IntegerField()
    carga_horaria = models.IntegerField()
    curso = models.CharField(max_length=255)
