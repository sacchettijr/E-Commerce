from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from usuario.forms import UsuarioCreationForm, UsuarioChangeForm
from usuario.models import Usuario, UsuarioEndereco


class UsuarioEnderecoInline(admin.TabularInline):
	model = UsuarioEndereco


@admin.register(Usuario)
class UsuarioAdmin(auth_admin.UserAdmin):
	model = Usuario
	list_display = [
		'email', 'telefone'
	]
	
	ordering = ['pk']
	
	add_form = UsuarioCreationForm
	add_fieldsets = (
		('Usuário', {
			'fields': {
				'email', ('password1', 'password2')
			}
		}),
		("Informações básicas", {
			"fields": (
				'nome', 'cpf_cnpj', 'data_nascimento', 'sexo', 'telefone'
			),
		}),
		("Permissões", {
			"fields": (
				('is_active', 'is_staff', 'is_superuser', 'is_trusty', 'is_anonymous'),
				'groups', 'user_permissions'
			),
		}),
	)
	
	form = UsuarioChangeForm
	fieldsets = (
		("Usuário", {
			"fields": (
				'email', 'password'
			),
		}),
		("Informações básicas", {
			"fields": (
				'nome', 'cpf_cnpj', 'data_nascimento', 'sexo', 'telefone'
			),
		}),
		("Permissões", {
			"fields": (
				('is_active', 'is_staff', 'is_superuser', 'is_trusty', 'is_anonymous'),
				'groups', 'user_permissions'
			),
		}),
	)
	
	inlines = [
		UsuarioEnderecoInline,
	]


@admin.register(UsuarioEndereco)
class UsuarioEndereco(admin.ModelAdmin):
	pass
