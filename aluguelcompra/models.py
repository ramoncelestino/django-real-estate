from django.db import models

class AluguelCompra(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome