from django.db import models


class ProdutoCategoria(models.Model):
	ativo = models.BooleanField(verbose_name='Ativo', default=False)
	nome = models.CharField(verbose_name='Nome', unique=True, max_length=255)
	slug = models.SlugField(verbose_name='URL', unique=True)
	descricao = models.CharField(verbose_name='Descrição', max_length=150, null=True, blank=True)
	imagem_destaque = models.ImageField(
		verbose_name='Imagem de destaque',
		upload_to='produto/categoria/',
		max_length=250, null=True, blank=True
	)

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
		db_table = 'produto_categoria'

	def __str__(self):
		return self.nome


class Produto(models.Model):
	
	# SITE
	ativo = models.BooleanField(default=False)
	slug = models.SlugField('Identificador', max_length=100)
	nome = models.CharField(max_length=255, unique=True)
	descricao = models.CharField(max_length=2000, null=True, blank=True)
	categoria = models.ForeignKey(ProdutoCategoria, on_delete=models.DO_NOTHING, null=True, blank=True)
	
	# VALOR
	valor_unitario = models.DecimalField(max_digits=15, decimal_places=2)
	
	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'
		db_table = 'produto'

	def __str__(self):
		return str(self.pk) + ' - ' + str(self.nome)
	
	
class ProdutoImagem(models.Model):
	produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=False, blank=False)
	padrao = models.BooleanField(default=False)
	imagem = models.ImageField(upload_to='produto/produto', max_length=255, null=False, blank=False)
	alt = models.CharField(max_length=150, default='Imagem de produto', null=True, blank=True)
	ativo = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Imagem do produto'
		verbose_name_plural = 'Imagens dos produtos'
		db_table = 'produto_imagem'

	def __str__(self):
		return str(self.pk) + ' - ' + str(self.produto)

	def save(self):

		#  SÓ UMA IMAGEM COMO PADRÃO
		if self.padrao:
			produto_imagens = ProdutoImagem.objects.filter(padrao=True, produto=self.produto.pk)
			for produto_imagem in produto_imagens:
				produto_imagem.padrao = False
				produto_imagem.save()
		super().save()
	