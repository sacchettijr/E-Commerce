from django.conf import settings
from django.db import models

from produto.models import Produto

Usuario = settings.AUTH_USER_MODEL


class CarrinhoItemManager(models.Manager):

	def add_item(self, chave_carrinho, produto):
		
		if self.filter(chave_carrinho=chave_carrinho, produto=produto).exists():
			created = False
			carrinho_item = self.get(chave_carrinho=chave_carrinho, produto=produto)
			carrinho_item.quantidade = carrinho_item.quantidade + 1
			carrinho_item.save()
		else:
			created = True
			carrinho_item = CarrinhoItem.objects.create(
				chave_carrinho=chave_carrinho,
				produto=produto,
				valor_unitario=produto.valor_unitario
			)
		
		return carrinho_item, created


class CarrinhoItem(models.Model):
	chave_carrinho = models.CharField('Chave do carrinho', max_length=40)
	produto = models.ForeignKey(Produto, verbose_name='Produto', on_delete=models.DO_NOTHING)
	quantidade = models.PositiveIntegerField('Quantidade', default=1)
	valor_unitario = models.DecimalField('Valor unitário', max_digits=15, decimal_places=2)
	
	# LOG
	data_atualizado = models.DateTimeField('Data da ultima modificação', auto_now=True, null=True, blank=True)
	data_criacao = models.DateTimeField('Data de criação', auto_now_add=True, null=True, blank=True)
	
	objects = CarrinhoItemManager()
	
	class Meta:
		db_table = 'carrinho_item'
		verbose_name = 'Item do carrinho'
		verbose_name_plural = 'Itens do carrinho'
		unique_together = (
			(
				'chave_carrinho',
				'produto'
			),
		)
	
	def __str__(self):
		return 'ID: {} - Produto: {}'.format(str(self.pk), str(self.produto.nome))
