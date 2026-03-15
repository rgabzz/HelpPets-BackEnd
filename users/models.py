from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.db import models

'''
AbstractBaseUser -  Traz a base de Usuário pronto, so precisando adicionar os outros campos
'''

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
        ('policia', 'Policia'),
        ('admin', 'Admin')
        )

    email  = models.EmailField(unique=True)
    
    genero = models.CharField(max_length=20)
    nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True,null=True,blank=True)
    
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    
    tipo =  models.CharField(max_length=10, choices=TIPO_USUARIO)

    '''
    USERNAME_FIELD - Diz pro django que o email também será usado para login
    REQUIRED_FIELDS - Diz pro comando de createsuperuser, que username também sera requisitadop
    '''

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
