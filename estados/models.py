from django.db import models

class Estado(models.Model):
    nome  = models.CharField(max_length=30)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome