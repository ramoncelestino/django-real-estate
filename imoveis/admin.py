from django.contrib import admin
from .models import Imovel, Bairro, Cidade, Estado, AluguelCompra

admin.site.register(Imovel)
admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(AluguelCompra)
