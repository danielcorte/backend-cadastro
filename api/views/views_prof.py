from django.shortcuts import render
from ..models import Professores
from ..serializer import ProfessoresSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

@api_view(['GET', 'POST'])
def listar_professores(request):
    if request.method == 'GET':
        queryset = Professores.objects.all()
        serializer = ProfessoresSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ProfessoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfessoresView(ListCreateAPIView):
    queryset = Professores.objects.all()
    serializer_class = ProfessoresSerializer
    permission_classes = [IsAuthenticated]

class ProfessoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Professores.objects.all()
    serializer_class = ProfessoresSerializer


class ProfessoresSearchView(ListAPIView):
    queryset = Professores.objects.all()
    serializer_class = ProfessoresSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['nome']

class CadastroFilter(django_filters.FilterSet):
    ni = django_filters.CharFilter(lookup_expr='icontains')
    nome = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    cel = django_filters.CharFilter(lookup_expr='icontains')
    ocup = django_filters.NumberFilter()
    ocup__gt = django_filters.NumberFilter(field_name='ocup', lookup_expr='gt')
    ocup__lt = django_filters.NumberFilter(field_name='ocup', lookup_expr='lt')

    class Meta:
        model = Professores
        fields = ['ni', 'nome', 'email', 'cel', 'ocup']

def product_list(request):
    f = CadastroFilter(request.GET, queryset=Professores.objects.all)
    return render(request, 'teachers_list.html', {'filter': f})

# def procurar_professores(request):

#     query = request.GET.get('search', '')

#     if query:
#         teachers = Cadastro.objects.filter(nome__icontains=query)

#     else:
#         teachers = Cadastro.objects.all()

#     return render(request, 'teachers_list.html', {'teachers':teachers, 'query':query})