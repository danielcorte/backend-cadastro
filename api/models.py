from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

class Professores(models.Model):
    ni = models.CharField(max_length=10, unique=True)
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

class Cursos(models.Model):
    CURSO_CHOICES = [
        ('cai', 'CAI'),
        ('tec', 'TEC'),
        ('fic', 'FIC') 
    ]

    sigla = models.CharField(max_length=8)
    nome = models.CharField(max_length=255)
    tipo_curso = models.CharField(
        max_length=10, choices=CURSO_CHOICES,
        default='tec'
    )
    minu_aula = models.IntegerField(validators=[MaxValueValidator(60)])

    def __str__(self):
        return f'{self.nome} - {self.sigla}'

class Ambientes(models.Model):
    PERIODO_CHOICES = [
    ('manha', 'Manhã'),
    ('tarde', 'Tarde'),
    ('noite', 'Noite')
    ]

    sala = models.CharField(max_length=8)
    prof_resp = models.ForeignKey(Professores, on_delete=models.CASCADE)
    capacidade = models.IntegerField(validators=[MaxValueValidator(140)])
    lin_atend = models.CharField(max_length=255)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, default="")
    materia = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, default="")
    inicio = models.DateField(default=timezone.now)
    fim = models.DateField(default=timezone.now)
    periodo = models.CharField(
    max_length=5, choices=PERIODO_CHOICES,
    default='manha', help_text="Escolha o período da turma: Manhã, Tarde ou Noite."
    )
