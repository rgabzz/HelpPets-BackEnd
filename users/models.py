from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.db import models

'''
AbstractBaseUser -  Traz a base de Usuário pronto, so precisando adicionar os outros campos
'''

# Rever essa questão do tipo do usuário estar na rota, e adicionar cadastero de ong

class User(AbstractUser): 

    '''
    --------------------------------------------------------------------------------------------------
     Essa função vai criar o modelo base para a parte do aplicativo relacionada aos dados do usuário.
    --------------------------------------------------------------------------------------------------

    + Ela cria a tabela de usuário em si, com todos os campos necessário para os primeiros testes do help pets (15/03/2026)
    
    '''

    TIPO_USUARIO = (
        ('usuario', 'Usuário'),
        ('ong', 'ONG'),
        #('policia', 'Policia'),
        )

    email  = models.EmailField(unique=True)
    
    genero = models.CharField(max_length=20)
    nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True,null=True,blank=True)
    
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    
    tipo =  models.CharField(max_length=10, choices=TIPO_USUARIO, default='usuario')

    '''
    USERNAME_FIELD - Diz pro django que o email também será usado para login
    REQUIRED_FIELDS - Diz pro comando de createsuperuser, que username também sera requisitado
    '''

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email



class Ong(models.Model):

    usuario = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name='perfil_ONG',
        null=False,
    )

    endereco  = models.CharField(max_length=255, null=False)

    pix = models.CharField(max_length=255, null=False)

    instagram  = models.CharField(max_length=255, null=False)

    descricao = models.TextField(null=False)

    def __str__(self):
            return self.descricao


