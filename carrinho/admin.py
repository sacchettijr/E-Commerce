from django.contrib import admin
from carrinho.models import Carrinho


@admin.register(Carrinho)
class Carrinho(admin.ModelAdmin):
	pass
