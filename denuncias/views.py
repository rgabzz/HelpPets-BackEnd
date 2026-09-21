from denuncias.models import Denuncias
from denuncias.serializers import DenunciasSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,generics
from rest_framework import permissions
from .filters import DenunciasFilter
from .permissions import DenunciasPermission

class DenunciasViewset(viewsets.ModelViewSet):
    serializer_class = DenunciasSerializer
    queryset = Denuncias.objects.all()
    
    filter_backends = [DjangoFilterBackend]

    filterset_class = DenunciasFilter

    def perform_create(self, serializer):
        # bloqueia o usuario de poder colocar a denuncia ja com uma ong pre pronta, alem de proibir alguem de colocar outro id de usuario apra aquela denuncia
        serializer.save(usuario=self.request.user, ong=None, status='aberto')

    permission_classes = [permissions.IsAuthenticated, DenunciasPermission]
