from django.contrib import admin
from .models import Produtos, Clientes


class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Clientes, ClienteAdmin)
