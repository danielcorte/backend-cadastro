# Generated by Django 5.1.5 on 2025-03-31 17:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_turmas_alter_ambientes_periodo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='minu_aula',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(60)]),
        ),
    ]
