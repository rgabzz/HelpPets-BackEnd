from rest_framework import permissions

class IsOwnerorAdmin(permissions.BasePermission):

    '''
    ------------------------------------------------------------------------------------------------------------------
     Essa classe foi criada para ser uma das permissões daquela aba especifica da API, relacionada a aba de usuários:
    ------------------------------------------------------------------------------------------------------------------
    
    + Só pode acessar o dono do perfil, ou o superusuario/admin
    + request.user.is_superuser - questiona se o usuário logado atualmente é admin
    + obj == request.user - questiona se o usuário daquela aba da API é igual ao usuário logado
    
    '''

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        
        return obj == request.user