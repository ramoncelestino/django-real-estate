from django.db import models
from cidades.models import Cidade

class Bairro(models.Model):
    nome   = models.CharField(max_length=30)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.nome