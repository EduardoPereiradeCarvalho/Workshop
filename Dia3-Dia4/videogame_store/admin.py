from django.contrib import admin
from .models import Jogo, Loja, Cliente

class JogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

admin.site.register(Jogo, JogoAdmin)

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Loja, LojaAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Cliente, ClienteAdmin)
