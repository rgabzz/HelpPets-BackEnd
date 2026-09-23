from django.contrib import admin
from denuncias.models import Denuncias

class VisualizarDenuncias(admin.ModelAdmin):
    
    '''
    -----------------------------------------------------------------------
     Essa função serve para a tabela de usuários aparecer na aba de admin:
    -----------------------------------------------------------------------

    + list_display - Quais partes da tabela vão aparecer
    + list_display_links - Quais ficam clicáveis
    + list_per_page - Quantos usuários vão aparecer por página
    + search_fields - Qual dos fields vc consegue pesquisar
    
    '''

    list_display = ('id', 'titulo_caixinha', 'midia_path', 'tipo_animal','quantidade','latitude','longitude','cidade','condicao','descricao','motivo','data_encontro','data_status_aceito','status','ong','criado_em','usuario',)
    list_display_links = ('titulo_caixinha',)
    list_per_page = 10
    search_fields = ('usuario','titulo_caixinha','ong','condicao','data_encontro')

admin.site.register(Denuncias, VisualizarDenuncias)
