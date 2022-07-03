from django.urls import reverse_lazy
from django.views.generic import CreateView
from usuario.forms import UsuarioCreationForm


class UsuarioCadastro(CreateView):
	template_name = 'registration/signup.html'
	form_class = UsuarioCreationForm
	success_url = reverse_lazy("login")

	