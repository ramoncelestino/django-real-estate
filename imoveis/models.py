from django.db import models
from tipoimoveis.models import TipoImovel


class Estado(models.Model):
    nome = models.CharField(max_length=30)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=40)
    estado = models.ForeignKey(
        Estado, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.nome


class Bairro(models.Model):
    nome = models.CharField(max_length=30)
    cidade = models.ForeignKey(
        Cidade, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.nome


class AluguelCompra(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    nome = models.CharField(max_length=30)
    description = models.TextField()
    tipo_imovel = models.ForeignKey(
        TipoImovel, on_delete=models.DO_NOTHING, null=True, blank=True)
    aluguel_compra = models.ForeignKey(
        AluguelCompra, on_delete=models.DO_NOTHING, null=True, blank=True)
    data_cadastro = models.DateTimeField()
    rua = models.CharField(max_length=40, default=False, null=True, blank=True)
    cep = models.CharField(max_length=40, default=False, null=True, blank=True)
    bairro = models.ForeignKey(
        Bairro, on_delete=models.DO_NOTHING, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quartos = models.IntegerField()
    banheiros = models.IntegerField()
    sqft = models.IntegerField(default=0)
    garagem = models.IntegerField(default=0)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.nome
