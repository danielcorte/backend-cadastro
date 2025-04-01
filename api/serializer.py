from rest_framework import serializers
from .models import Professores, Disciplinas, Ambientes, Cursos, Turmas
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

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

class TurmasSerializer(serializers.ModelSerializer):
    class Meta:

        model = Turmas
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)