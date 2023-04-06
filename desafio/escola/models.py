from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length = 100)
    turma = models.CharField(max_length = 100)

    def _str_(self):
        return self.nome
    
class Disciplina(models.Model):
    nome = models.CharField(max_length = 100)
    
    def _str_(self):
        return self.nome
