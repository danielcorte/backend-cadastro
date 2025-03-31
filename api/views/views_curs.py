from django.shortcuts import render
from ..models import Cursos
from ..serializer import CursosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# import django_filters


@api_view(['GET', 'POST'])
def listar_cursos(request):
    if request.method == 'GET':
        queryset = Cursos.objects.all()
        serializer = CursosSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CursosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CursosView(ListCreateAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
    permission_classes = [IsAuthenticated]


class CursosDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer


class CursosSearchView(ListAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['nome']


# class CursosFilter(django_filters.FilterSet):
#     sigla = django_filters.CharFilter(lookup_expr='icontains')
#     nome = django_filters.CharFilter(lookup_expr='icontains')
#     curso = django_filters.NumberFilter()
#     semestre = django_filters.NumberFilter(lookup_expr='icontains')
#     smtr__gt = django_filters.NumberFilter(field_name='semestre', lookup_expr='gt')
#     smtr__lt = django_filters.NumberFilter(field_name='semestre', lookup_expr='lt')
#     carga_horaria = django_filters.NumberFilter(lookup_expr='icontains')
#     ch__gt = django_filters.NumberFilter(field_name='carga_horaria', lookup_expr='gt')
#     ch__lt = django_filters.NumberFilter(field_name='carga_horaria', lookup_expr='lt')

#     class Meta:
#         model = Cursos
#         fields = ['sigla', 'nome', 'semestre', 'carga_horaria', 'curso']

# def product_list(request):
#     f = CursosFilter(request.GET, queryset=Cursos.objects.all)
#     return render(request, 'teachers_list.html', {'filter': f})