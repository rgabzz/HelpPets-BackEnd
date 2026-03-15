from django.contrib import admin
from users.models import User

class VisualizarUsuarios(admin.ModelAdmin):
    
    '''
    -----------------------------------------------------------------------
     Essa função serve para a tabela de usuários aparecer na aba de admin:
    -----------------------------------------------------------------------

    + list_display - Quais partes da tabela vão aparecer
    + list_display_links - Quais ficam clicáveis
    + list_per_page - Quantos usuários vão aparecer por página
    + search_fields - Qual dos fields vc consegue pesquisar
    
    '''

    list_display = ('id', 'username', 'email', 'nascimento',)
    list_display_links = ('username',)
    list_per_page = 10
    search_fields = ('username',)

admin.site.register(User, VisualizarUsuarios)
