from django.contrib.auth import forms
from usuario.models import Usuario


class UsuarioCreationForm(forms.UserCreationForm):
	class Meta(forms.UserCreationForm.Meta):
		model = Usuario
		fields = ['email', 'password1', 'password2', 'nome', 'cpf_cnpj', 'telefone', 'data_nascimento', 'sexo']
		

class UsuarioChangeForm(forms.UserChangeForm):
	class Meta(forms.UserChangeForm.Meta):
		model = Usuario
		fields = '__all__'
