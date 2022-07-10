from django.conf import settings
from django.db import models

from produto.models import Produto

Usuario = settings.AUTH_USER_MODEL


class Carrinho(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
	produto = models.ManyToManyField(Produto, blank=True)
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	
	data_atualizado = models.DateTimeField(verbose_name="Data da ultima modificação", auto_now=True)
	data_criacao = models.DateTimeField(verbose_name="Data de criação", auto_now_add=True)
	
	def __str__(self):
		return str(self.id)
