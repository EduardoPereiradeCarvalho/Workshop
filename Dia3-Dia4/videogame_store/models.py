from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length = 100)
    preco = models.DecimalField(max_digits = 7, decimal_places = 2)

    def _str_(self):
        return self.nome
    
class Loja(models.Model):
    nome = models.CharField(max_length = 100)
    endereco = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 11)

    def _str_(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField(max_length = 100)
    endereco = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 11)

    def _str_(self):
        return self.nome
