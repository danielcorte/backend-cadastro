from django.shortcuts import render
from ..models import Turmas
from ..serializer import TurmasSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

@api_view(['GET', 'POST'])
def listar_turmas(request):
    if request.method == 'GET':
        queryset = Turmas.objects.all()
        serializer = TurmasSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = TurmasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TurmasView(ListCreateAPIView):
    queryset = Turmas.objects.all()
    serializer_class = TurmasSerializer
    permission_classes = [IsAuthenticated]

class TurmasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Turmas.objects.all()
    serializer_class = TurmasSerializer


class TurmasSearchView(ListAPIView):
    queryset = Turmas.objects.all()
    serializer_class = TurmasSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['turma', 'cod_turma']
