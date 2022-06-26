import re
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from datetime import date
from django.core import validators
from django.core.mail import send_mail
from django.db import models

from geral.models import Endereco


class Usuario(AbstractBaseUser, PermissionsMixin):
	objects = UserManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'nome', 'cpf_cnpj']
	
	
	# USUÁRIO
	username = models.CharField(
		'Usuário', max_length=50, unique=True, validators=[
			validators.RegexValidator(
				re.compile('^[\w.@+-]+$'),
				'Informe um usuário válido.'
				'Este valor deve conter apenas letras e números '
				'e os caracteres @/./+/-/_.',
				'invalid'
			)
		], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
	)
	
	
	# CONTATO
	telefone = models.CharField('Telefone', max_length=20, null=True, blank=True)
	email = models.EmailField('E-Mail', unique=True)
	
	# PESSOAL
	nome = models.CharField('Nome', max_length=255, blank=True, null=True)
	cpf_cnpj = models.CharField('CPF/CNPJ', max_length=18, unique=True)
	data_nascimento = models.DateField('Data de Nascimento', default=date.today, null=True, blank=True)
	SEXO_CHOICES = (
		("M", "Masculino"),
		("F", "Feminino"),
		("N", "Nenhuma das opções")
	)
	sexo = models.CharField('Sexo', max_length=1, null=True, blank=True, choices=SEXO_CHOICES, default='N')
	
	# PERMISSÕES
	is_staff = models.BooleanField('Equipe', default=False)
	is_active = models.BooleanField('Ativo', default=True)
	is_superuser = models.BooleanField('Superusuário', default=False)
	is_anonymous = models.BooleanField('Anonimo', default=False)
	is_trusty = models.BooleanField('E-Mail confirmado', default=False)
	
	# LOG
	data_cadastro = models.DateTimeField('Data de cadastro', auto_now_add=True, null=True, blank=True)
	data_ultima_modificacao = models.DateTimeField('Data da ultima modificação', auto_now=True, null=True, blank=True)
	
	class Meta:
		db_table = 'usuario'
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'
	
	def __str__(self):
		return self.username or self.get_short_name()
	
	def get_full_name(self):
		return str(self.nome)
	
	def get_short_name(self):
		return str(self.nome).split(" ")[0]
	
	def email_user(self, subject, message, from_email=None):
		send_mail(subject, message, from_email, [self.email])


class UsuarioEndereco(Endereco):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	padrao = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Endereço do usuário'
		verbose_name_plural = 'Endereços dos usuários'
		db_table = 'usuario_endereco'

	def __str__(self):
		informacao = 'Usuário: ' + str(
			self.usuario) + ' - Endereço: ' + self.rua + ', nº ' + self.numero + ', ' + self.bairro + ', CEP ' + self.cep
		if self.complemento:
			informacao = informacao + ', ' + self.complemento
		if self.referencia:
			informacao = informacao + ', ' + self.referencia
		return informacao

	def save(self):
		#  SÓ UM ENDEREÇO COMO PADRÃO
		if self.padrao:
			usuarios_enderecos = UsuarioEndereco.objects.filter(padrao=True, produto=self.endereco.pk)
			for usuario_endereco in usuarios_enderecos:
				usuario_endereco.padrao = False
				usuario_endereco.save()
		super().save()
