from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produtos


def index(request):

    # print(f'Paramentros request: {dir(request.user)}')
    # print()
    # print(f'User: {request.user}')

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado.'
    else:
        teste = 'Usuário logado.'

    produtos = Produtos.objects.all()

    context = {
        'curso': 'Desenvolvimento Web com Python',
        'outro': 'Django é massa!',
        'Logado': teste,
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    # prod = Produtos.objects.get(id=pk)
    prod = get_object_or_404(Produtos, id=pk)

    context = {
        'produto': prod
    }

    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
