from adocoes.models import Animal,Adocao
from adocoes.serializers import AnimalSerializer,AdocaoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,generics
from rest_framework import permissions
from .filters import AnimalFilters
from .permissions import AdocoesPermissions, AnimalPermissions

class AnimalViewset(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnimalFilters

    permission_classes = [permissions.IsAuthenticated,AnimalPermissions]

class AdocaoViewset(viewsets.ModelViewSet):
    serializer_class = AdocaoSerializer
    queryset = Adocao.objects.all()

    permission_classes = [permissions.IsAuthenticated,AdocoesPermissions]