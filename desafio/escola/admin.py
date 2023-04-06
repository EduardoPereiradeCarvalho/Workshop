from django.contrib import admin
from .models import Estudante, Disciplina

class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turma')

admin.site.register(Estudante, EstudanteAdmin)

class DisciplinaAdmin(admin.ModelAdmin):
    list = ('nome')

admin.site.register(Disciplina, DisciplinaAdmin)
