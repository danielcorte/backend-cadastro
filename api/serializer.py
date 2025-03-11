from rest_framework import serializers
from .models import Professores, Disciplinas

class ProfessoresSerializer(serializers.ModelSerializer):
    class Meta:

        model = Professores
        fields = '__all__'


class DisciplinasSerializer(serializers.ModelSerializer):
    class Meta:

        model = Disciplinas
        fields = '__all__'
       