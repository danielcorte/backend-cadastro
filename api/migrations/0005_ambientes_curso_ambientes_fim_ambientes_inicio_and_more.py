# Generated by Django 5.1.5 on 2025-03-18 18:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_cursos_alter_professores_ni_ambientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambientes',
            name='curso',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.cursos'),
        ),
        migrations.AddField(
            model_name='ambientes',
            name='fim',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ambientes',
            name='inicio',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ambientes',
            name='materia',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.disciplinas'),
        ),
    ]
