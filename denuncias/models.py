from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.db import models
from django.conf import settings
from django.utils import timezone
from users.models import Ong


from multiselectfield import MultiSelectField

'''
AbstractBaseUser -  Traz a base de Usuário pronto, so precisando adicionar os outros campos
'''

# Rever essa questão do tipo do usuário estar na rota, e adicionar cadastero de ong
class Denuncias(models.Model): 

    '''
    --------------------------------------------------------------------------------------------------
     Essa função vai criar o modelo base para a parte do aplicativo relacionada aos dados dos chamados.
    --------------------------------------------------------------------------------------------------

    + Ela cria a tabela de chamados em si, com todos os campos necessário para os primeiros testes do help pets (29/03/2026)
    
    '''

    CONDICAO_CHOICES = (
        ('Bem / saudável', 'Bem / saudável'),
        ('Sujo', 'Sujo'),
        ('Muito magro', 'Muito magro'),
        ('Fraco / sem forças', 'Fraco / sem forças'),
        ('Dificuldade para andar', 'Dificuldade para andar'),
        ('Dificuldade para respirar', 'Dificuldade para respirar'),
        ('Parece doente', 'Parece doente'),
        ('Machucado', 'Machucado'),
        ('Sangrando', 'Sangrando'),
        ('Osso ou ferida aberta', 'Osso ou ferida aberta'),
        ('Inchaço ou caroços', 'Inchaço ou caroços'),
        ('Parasitas', 'Parasitas'),
        ('Sarna aparente', 'Sarna aparente'),
        ('Queda de pelo', 'Queda de pelo'),
        ('Assustado', 'Assustado'),
        ('Agressivo', 'Agressivo'),
        ('Muito quieto / parado', 'Muito quieto / parado'),
        ('Desorientado', 'Desorientado'),
        ('Perto de trânsito intenso', 'Perto de trânsito intenso'),
    )


    STATUS_DENUNCIA = (
        ('aberto', 'Aberto'),
        ('atendimento', 'Atendimento'),
        ('finalizado', 'Finalizado'),
        )
    
    titulo_caixinha = models.CharField(max_length=255,null=False)

    midia_path = models.CharField(max_length=255,null=False)

    tipo_animal = models.CharField(max_length=255,null=False)
    quantidade = models.IntegerField(null=False)

    latitude = models.DecimalField(max_digits=8,decimal_places=6,default=0.00)
    longitude = models.DecimalField(max_digits=9,decimal_places=6,default=0.00)
    cidade = models.CharField(max_length=255,null=False)
    
    condicao = MultiSelectField(choices=CONDICAO_CHOICES,max_length=500,default='Bem / saudável')
    
    descricao = models.TextField(null=False)

    motivo = models.CharField(max_length=255,null=False)

    data_encontro = models.DateTimeField(null=False,default=timezone.now)

    data_status_aceito = models.DateTimeField(null=True,default=timezone.now)

    status =  models.CharField(max_length=50, choices=STATUS_DENUNCIA)
    
    ong_id = models.ForeignKey(
        'users.Ong',
        on_delete=models.SET_NULL, 
        verbose_name="ONG ID",
        null=True
    )

    criado_em = models.DateTimeField(null=False,default=timezone.now)

    usuario_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name="Usuario ID"
    )
    
    def __str__(self):
        return self.titulo_caixinha
