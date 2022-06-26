from django.contrib import admin
from geral.models import Pais, Estado, Cidade


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
	pass


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	pass


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
	pass
