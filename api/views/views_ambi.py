from django.shortcuts import render
from ..models import Ambientes
from ..serializer import AmbientesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

@api_view(['GET', 'POST'])
def listar_ambientes(request):
    if request.method == 'GET':
        queryset = Ambientes.objects.all()
        serializer = AmbientesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = AmbientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AmbientesView(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    permission_classes = [IsAuthenticated]

class AmbientesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer


class AmbientesSearchView(ListAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['nome']

class AmbientesFilter(django_filters.FilterSet):
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
        model = Ambientes
        fields = ['sigla', 'nome', 'semestre', 'carga_horaria', 'curso']

def product_list(request):
    f = AmbientesFilter(request.GET, queryset=Ambientes.objects.all)
    return render(request, 'teachers_list.html', {'filter': f})