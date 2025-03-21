from rest_framework import serializers
from .models import Professores, Disciplinas, Ambientes, Cursos

class ProfessoresSerializer(serializers.ModelSerializer):
    class Meta:

        model = Professores
        fields = '__all__'


class DisciplinasSerializer(serializers.ModelSerializer):
    class Meta:

        model = Disciplinas
        fields = '__all__'
       
class CursosSerializer(serializers.ModelSerializer):
    class Meta:

        model = Cursos
        fields = '__all__'

class AmbientesSerializer(serializers.ModelSerializer):
    class Meta:

        model = Ambientes
        fields = '__all__'