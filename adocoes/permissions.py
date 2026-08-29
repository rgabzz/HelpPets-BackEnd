from rest_framework import permissions

class AnimalPermissions(permissions.BasePermission):    

    def has_permission(self, request, view):
        """
            Controle de acesso geral (Antes de pegar o objeto do banco)
        """

        perm_ong = (getattr(request.user, 'TIPO_USUARIO', None) == 'ONG')
        perm_admin = (request.user.is_superuser)
        
        # Se for POST (Criação), apenas ONGs ou Admins do sistema
        if request.method == 'POST':
            return perm_ong or perm_admin

        return True

    def has_object_permission(self, request, view, obj):
        """
            Controle de acesso ao objeto específico (Denúncia já existente)
        """

        perm_dono = (obj.ong.usuario == request.user)
        perm_ong = (getattr(request.user, 'TIPO_USUARIO', None) == 'ONG')
        perm_admin = (request.user.is_superuser)

        # 1. GET - Todos os Usuários
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # 2. PUT e PATCH - Apenas ONGs ou Admins do sistema
        if request.method == 'PUT' or  request.method == 'PATCH': 
            return perm_dono or perm_ong

        # 3. DELETE - Apenas Superuser
        if request.method == 'DELETE': 
            return perm_admin
        
class AdocoesPermissions(permissions.BasePermission):    

    def has_permission(self, request, view):
        """
            Controle de acesso geral (Antes de pegar o objeto do banco)
        """

        perm_ong = (getattr(request.user, 'TIPO_USUARIO', None) == 'ONG')
        perm_admin = (request.user.is_superuser)
        
        # Se for POST (Criação), apenas ONGs ou Admins do sistema
        if request.method == 'POST':
            return perm_ong or perm_admin

        return True

    def has_object_permission(self, request, view, obj):
        """
            Controle de acesso ao objeto específico (Denúncia já existente)
        """

        perm_admin = (request.user.is_superuser)

        # 1. GET - Apenas Admins
        if request.method in permissions.SAFE_METHODS:
            return perm_admin

        # 2. PUT e PATCH - Apenas Admins
        if request.method == 'PUT' or  request.method == 'PATCH': 
            return perm_admin

        # 3. DELETE - Apenas Admins
        if request.method == 'DELETE': 
            return perm_admin