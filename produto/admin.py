from django.contrib import admin
from produto.models import Categoria, Produto, ProdutoImagem


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	pass


class ProdutoImagemInline(admin.TabularInline):
	model = ProdutoImagem


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	inlines = [
		ProdutoImagemInline,
	]


@admin.register(ProdutoImagem)
class ProdutoImagemAdmin(admin.ModelAdmin):
	pass
