from django.db import models
from django.utils import timezone

class Animal(models.Model):
    STATUS = (
        ('disponivel','disponivel'),
        ('em_processo','em_processo'),
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
        on_delete=models.CASCADE,
        verbose_name="ONG",
        null=False
    )
    criado_em = models.DateTimeField(null=False, default=timezone.now)

class Adocao(models.Model):
    animal = models.ForeignKey(
            'adocoes.Animal',
            on_delete=models.CASCADE, 
            verbose_name="ÀNIMAL",
            null=True 
       )

    ong = models.ForeignKey(
            'users.Ong',
            on_delete=models.SET_NULL, 
            verbose_name="ONG",
            null=True
           )

    usuario = models.ForeignKey(
            'users.User',
            on_delete=models.SET_NULL, 
            verbose_name="Usuario",
            null=True
        )
       
    data_adocao = models.DateTimeField(null=False, default=timezone.now)
