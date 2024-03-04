from django.db import models
from necessario.models import *

DIVISAO_CHOICES = (
  ('A', 'Série A'),
  ('B', 'Série B'),
  ('C', 'Série C'),
  ('D', 'Série D'),
  ('S', 'Sem Série'),
)

MODALIDADE_CHOICES = (
  ('M', 'Masculino'),
  ('F', 'Feminino')
)

class Clube(models.Model):
  nome = models.CharField(max_length=128, blank=False, null=False)
  ano_fundacao = models.PositiveIntegerField('Ano Fundação', help_text="Ano que o Clube foi criado")
  divisao = models.CharField('Divisão', max_length=64, choices=DIVISAO_CHOICES, default='S', blank=False, null=True)
  modalidade = models.CharField(choices=MODALIDADE_CHOICES, max_length=2, default='F')

  cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)

  class Meta:
    verbose_name = 'Clube'
    verbose_name_plural = 'Clubes'

  def __str__(self):
    return self.nome


class Jogador(models.Model):
  nome = models.CharField(max_length=128, blank=False, null=False)
  numero_camisa = models.PositiveIntegerField()

  clube = models.ForeignKey(Clube, on_delete=models.CASCADE, null=False, blank=False)

  class Meta:
    verbose_name_plural = 'Jogadores'

  def __str__(self):
    return self.nome
