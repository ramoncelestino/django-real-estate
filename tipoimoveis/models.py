from django.db import models

class TipoImovel(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome