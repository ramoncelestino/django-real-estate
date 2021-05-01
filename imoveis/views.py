from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Imovel, Bairro, AluguelCompra
from tipoimoveis.models import TipoImovel
from .form import ImovelForm
# Create your views here.


def index(request):
    queryset_list = Imovel.objects.order_by('-data_cadastro')[:3]

    tipos = TipoImovel.objects.all()
    bairros = Bairro.objects.all()
    modelos = AluguelCompra.objects.all()
    faixas_preco = ['1000', '5000', '10000']

    context = {
        'list_imoveis': queryset_list,
        'bairros': bairros,
        'faixas_preco': faixas_preco,
        'tipos': tipos,
        'modelos': modelos,
        'values': request.GET
    }

    return render(request, 'index.html', context)


def search_imoveis(request):
    queryset_list = Imovel.objects.order_by('-price')

    tipos = TipoImovel.objects.all()
    bairros = Bairro.objects.all()
    modelos = AluguelCompra.objects.all()
    faixas_preco = ['1000', '5000', '10000']
    updown = ""

    if 'bairro' in request.GET:
        bairro = request.GET['bairro']
        if bairro:
            queryset_list = queryset_list.filter(
                bairro__nome__icontains=bairro)

    if 'preco' in request.GET:
        preco = request.GET['preco']
        if preco:
            queryset_list = queryset_list.filter(price__lte=preco)

    if 'tipo' in request.GET:
        tipo = request.GET['tipo']
        if tipo:
            queryset_list = queryset_list.filter(
                tipo_imovel__nome__icontains=tipo)

    if 'modelo' in request.GET:
        modelo = request.GET['modelo']
        if modelo:
            queryset_list = queryset_list.filter(
                aluguel_compra__nome__icontains=modelo)

    if 'updown' in request.GET:
        updown = request.GET['updown']

    if 'order' in request.GET:
        order = request.GET['order']

        if order:
            queryset_list = queryset_list.order_by(updown + order)

    order_types = ['name', 'price', 'date']

    context = {
        'bairros': bairros,
        'faixas_preco': faixas_preco,
        'tipos': tipos,
        'modelos': modelos,
        'listings': queryset_list,
        'order_types': order_types,
        'values': request.GET
    }

    return render(request, 'search_imoveis.html', context)


def lancamentos(request):

    list_imoveis = Bairro.objects.all()[:2]

    context = {
        'list_imoveis': list_imoveis
    }

    return render(request, 'lancamentos.html', context)


def create_imovel(request):

    form = ImovelForm()

    if request.method == 'POST':
        form = ImovelForm(request.POST or None)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'create_imovel.html', context)


def view_imovel(request, pk):
    imovel = Imovel.objects.get(id=pk)

    context = {'imovel': imovel}

    return render(request, 'view_imovel.html', context)


def view_apresentacao(request):
    return render(request, 'apresentacao.html', {})


class ImovelListView(ListView):
    queryset = Imovel.objects.all()


def delete_imovel(request, pk):
    Imovel.objects.get(id=pk).delete()

    return redirect('imoveis')


def update_imovel(request, pk):
    pass


def login(request):
    return render(request, 'login.html', {})
