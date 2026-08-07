from django.db import models
from django.utils import timezone

class Animal(models.Model):
    STATUS = (
        ('disponivel','disponivel'),
        ('adotado','adotado'),
        )
    nome = models.CharField(max_length=255, default= 'Desconhecido')
    especie = models.CharField(max_length=255, default= 'Desconhecido')
    raca = models.CharField(max_length=255, default= 'Desconhecido')
    idade = models.CharField(max_length=255, default= 'Desconhecido')
    descricao = models.TextField(max_length=255, )
    status_adocao = models.CharField(max_length=50, choices=STATUS)
    ong = models.ForeignKey(
        'users.Ong',
        on_delete=models.SET_NULL, 
        verbose_name="ONG",
        null=True
    )
    criado_em = models.DateTimeField(null=False, default=timezone.now)