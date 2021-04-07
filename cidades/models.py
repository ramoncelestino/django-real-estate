from django.db import models
from estados.models import Estado

class Cidade(models.Model):
    nome   = models.CharField(max_length=40)
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.nome