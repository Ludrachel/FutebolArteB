from django.contrib import admin
from futebol.models import Clube, Jogador
from necessario.models import Cidade

class JogadorInline(admin.StackedInline):
  model = Jogador
  extra = 0

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
  search_fields = ['nome']


@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
  list_display = ['nome', 'cidade', 'ano_fundacao', 'divisao']
  list_display_links = ['nome']
  autocomplete_fields = ['cidade']
  list_filter = ['divisao']
  search_fields = ['nome', 'cidade__nome']
  
  inlines = [JogadorInline]

