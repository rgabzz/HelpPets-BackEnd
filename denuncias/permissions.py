from rest_framework import permissions

class DenunciasPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Controle de acesso geral (Antes de pegar o objeto do banco)
        """

        # Se for POST (Criação), qualquer usuário autenticado pode (ou mude para True se for público)
        if request.method == 'POST':  
            return request.user and request.user.is_authenticated
        
        return True


    def has_object_permission(self, request, view, obj):
        """
        Controle de acesso ao objeto específico (Denúncia já existente)
        """

        perm_dono = (obj.usuario == request.user)
        perm_ong = (getattr(request.user, 'TIPO_USUARIO', None) == 'ONG')
        perm_admin = (request.user.is_superuser)

        # 1. GET - Apenas ONG e Usuário que criou e super user
        if request.method in permissions.SAFE_METHODS: 
            return perm_ong or perm_dono or perm_admin

        # 2. PUT e PATCH - Apenas ONG e Usuário que criou e superuser
        if request.method == 'PUT' or  request.method == 'PATCH': 
            return perm_ong or perm_dono or perm_admin

        # 3. DELETE - Apenas Superuser
        if request.method == 'DELETE': 
            return perm_admin
