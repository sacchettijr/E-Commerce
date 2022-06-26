from django.contrib.auth import forms
from usuario.models import Usuario


class UsuarioCreationForm(forms.UserCreationForm):
	class Meta(forms.UserCreationForm.Meta):
		model = Usuario
		fields = '__all__'
		

class UsuarioChangeForm(forms.UserChangeForm):
	class Meta(forms.UserChangeForm.Meta):
		model = Usuario
		fields = '__all__'
