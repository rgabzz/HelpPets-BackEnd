from django.contrib import admin
from adocoes.models import Adocao,Animal

class VisualizarAnimal(admin.ModelAdmin):
    
    '''
    -----------------------------------------------------------------------
     Essa função serve para a tabela de usuários aparecer na aba de admin:
    -----------------------------------------------------------------------

    + list_display - Quais partes da tabela vão aparecer
    + list_display_links - Quais ficam clicáveis
    + list_per_page - Quantos usuários vão aparecer por página
    + search_fields - Qual dos fields vc consegue pesquisar
    
    '''

    list_display = ('id', 'nome', 'especie', 'raca','idade','descricao','status_adocao','ong','criado_em',)
    list_display_links = ('nome',)
    list_per_page = 10
    search_fields = ('nome','especie','raca','status_adocao','ong')

class VisualizarAdocoes(admin.ModelAdmin):
    
    '''
    -----------------------------------------------------------------------
     Essa função serve para a tabela de usuários aparecer na aba de admin:
    -----------------------------------------------------------------------

    + list_display - Quais partes da tabela vão aparecer
    + list_display_links - Quais ficam clicáveis
    + list_per_page - Quantos usuários vão aparecer por página
    + search_fields - Qual dos fields vc consegue pesquisar
    
    '''

    list_display = ('id', 'animal', 'ong', 'usuario',)
    list_display_links = ('animal','ong','usuario',)
    list_per_page = 10
    search_fields = ('animal','ong','ong','usuario',)

admin.site.register(Adocao, VisualizarAdocoes)
admin.site.register(Animal, VisualizarAnimal)