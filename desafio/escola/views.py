from rest_framework import viewsets
from .serializer import EstudanteSerializer, DisciplinaSerializer
from .models import Estudante, Disciplina

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer 

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
