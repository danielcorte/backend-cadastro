from django.shortcuts import render
from ..models import Disciplinas
from ..serializer import DisciplinasSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

@api_view(['GET', 'POST'])
def listar_disciplinas(request):
    if request.method == 'GET':
        queryset = Disciplinas.objects.all()
        serializer = DisciplinasSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = DisciplinasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DisciplinasView(ListCreateAPIView):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinasSerializer
    permission_classes = [IsAuthenticated]

class DisciplinasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinasSerializer


class DisciplinasSearchView(ListAPIView):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinasSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['id', 'nome', 'sigla', 'carga_horaria', 'curso']
         

        

class DisciplinaFilter(django_filters.FilterSet):
    id = django_filters
    sigla = django_filters.CharFilter(lookup_expr='icontains')
    nome = django_filters.CharFilter(lookup_expr='icontains')
    curso = django_filters.NumberFilter()
    semestre = django_filters.NumberFilter(lookup_expr='icontains')
    smtr__gt = django_filters.NumberFilter(field_name='semestre', lookup_expr='gt')
    smtr__lt = django_filters.NumberFilter(field_name='semestre', lookup_expr='lt')
    carga_horaria = django_filters.NumberFilter(lookup_expr='icontains')
    ch__gt = django_filters.NumberFilter(field_name='carga_horaria', lookup_expr='gt')
    ch__lt = django_filters.NumberFilter(field_name='carga_horaria', lookup_expr='lt')

    class Meta:
        model = Disciplinas
        fields = ['sigla', 'nome', 'semestre', 'carga_horaria', 'curso']

def product_list(request):
    f = DisciplinaFilter(request.GET, queryset=Disciplinas.objects.all)
    return render(request, 'teachers_list.html', {'filter': f})