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
        ('ct', 'CT'),
        ('fic', 'FIC'),
        ('cs', 'CS')
    ]

    sigla = models.CharField(max_length=8)
    nome = models.CharField(max_length=255)
    tipo_curso = models.CharField(
        max_length=10, choices=CURSO_CHOICES,
        default='ct'
    )
    minu_aula = models.IntegerField()

    def __str__(self):
        return f'{self.nome} - {self.sigla}'

class Ambientes(models.Model):
    PERIODO_CHOICES = [
    ('manha', 'Manhã'),
    ('tarde', 'Tarde'),
    ('noite', 'Noite'),
    ('sabado', 'Sábado')
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
    max_length=6, choices=PERIODO_CHOICES,
    default='manha', help_text="Escolha o período da turma: Manhã, Tarde ou Noite."
    )

class Turmas(models.Model):
    cod_turma = models.CharField(max_length=8)
    turma = models.CharField(max_length=255)

