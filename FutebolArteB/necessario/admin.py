from django.contrib import admin
from necessario.models import Pais, Estado, Cidade

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
  list_display = ['nome']


class CidadeInline(admin.TabularInline):
  model = Cidade
  extra = 0

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'sigla']
  inlines = [CidadeInline]
