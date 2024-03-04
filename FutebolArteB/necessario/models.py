from django.db import models

class Pais(models.Model):
  nome = models.CharField(max_length=128)

  class Meta:
    verbose_name_plural = 'Países'

  def __str__(self):
    return self.nome


class Estado(models.Model):
  nome = models.CharField(max_length=128)
  sigla = models.CharField(max_length=2, null=True, blank=False)

  pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=False, blank=False)

  def __str__(self):
    return self.nome


class Cidade(models.Model):
  nome = models.CharField(max_length=128)

  estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return f'{self.nome} - {self.estado.sigla} - {self.estado.pais.nome}'

