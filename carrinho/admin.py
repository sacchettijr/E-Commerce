from django.contrib import admin
from carrinho.models import CarrinhoItem


@admin.register(CarrinhoItem)
class CarrinhoItemAdmin(admin.ModelAdmin):
	pass
