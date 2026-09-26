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

    def perform_create(self, serializer):
        ong = getattr(self.request.user, 'perfil_ONG', None) 
        serializer.save(ong=ong)
  
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnimalFilters

    permission_classes = [permissions.IsAuthenticated,AnimalPermissions]

class AdocaoViewset(viewsets.ModelViewSet):
    serializer_class = AdocaoSerializer
    queryset = Adocao.objects.all()

    def get_queryset(self):

            user = self.request.user
    
            ''' 
                Verificação criada para que nenhum usuário consiga acessar a lista com todos as adocoes
            - Sem essa verificação a rota /adocoes/ fica exposta e todos conseguem acessar as informações dos usuários
            - Com ela apenas admins conseguem ver isso, caso o usuário comum tente acessar, encontrará apenas suas adocões
    
            '''
    
            if user.is_superuser:
                return Adocao.objects.all().order_by('id')

            if user.tipo == 'ong':
                ong_perfil  = getattr(user, 'perfil_ONG', None)

                if ong_perfil  is None:
                    return Adocao.objects.none()

                return Adocao.objects.filter(ong=ong_perfil )
                 
            
            return Adocao.objects.filter(usuario=user)

    def perform_create(self, serializer):
            ong = getattr(self.request.user, 'perfil_ONG', None) 
            serializer.save(ong=ong)

    permission_classes = [permissions.IsAuthenticated,AdocoesPermissions]