from django.db import models

class BuscarRaças(models.Model):

    nome_raça = models.CharField(max_length=20, unique=True)
    tamanho = models.CharField(max_length=20)
    inteligencia = models.CharField(max_length=20)
    expectativa_de_vida = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_raça
