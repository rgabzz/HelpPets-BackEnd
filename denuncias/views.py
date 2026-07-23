from denuncias.models import Denuncias
from denuncias.serializers import DenunciasSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,generics
from rest_framework import permissions

class DenunciasViewset(viewsets.ModelViewSet):
    serializer_class = DenunciasSerializer
    queryset = Denuncias.objects.all()
    
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['cidade']