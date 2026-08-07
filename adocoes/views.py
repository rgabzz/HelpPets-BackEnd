from adocoes.models import Animal
from adocoes.serializers import AnimalSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,generics
from rest_framework import permissions

class AnimalViewset(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['especie','raca','ong','status_adocao']

    permission_classes = [permissions.IsAuthenticated]