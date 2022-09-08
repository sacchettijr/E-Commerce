from requests import request
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import CreateView, UpdateView, TemplateView, FormView
from usuario.forms import UsuarioCreationForm, UsuarioChangeForm


class UsuarioCadastroView(CreateView):
	template_name = 'registration/signup.html'
	form_class = UsuarioCreationForm
	success_url = reverse_lazy("login")


class UsuarioPerfilIndexView(LoginRequiredMixin, TemplateView):
	template_name = 'conta/publico_minha_conta.html'

	def get_context_data(self, **kwargs):
		print('\n'*20 + '_'*80 + '\n\n VIEW: UsuarioPerfilIndex \n')

		usuario_id = str(self.request.user.pk)
		print('\nPRINT >>> ID Usuário = {}\n'.format(usuario_id))

		self.kwargs['conta_index'] = True
		return self.kwargs


class UsuarioPerfilAtualizarSenhaView(LoginRequiredMixin, FormView):
	template_name = 'conta/publico_atualizar_senha.html'
	success_url = reverse_lazy('publico_minha_conta_atualizar_senha')
	form_class = PasswordChangeForm

	def get_form_kwargs(self):
		print('\n'*20 + '_'*80 + '\n\n VIEW: UsuarioPerfilAtualizarSenhaView \n')

		kwargs = super(UsuarioPerfilAtualizarSenhaView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs


id_old_password
id_new_password1
id_new_password2

class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class UsuarioPerfilEditarView(LoginRequiredMixin, TemplateView):
	template_name = 'conta/publico_minha_conta_editar.html'

	def get_context_data(self, **kwargs):
		print('\n'*20 + '_'*80 + '\n\n VIEW: UsuarioPerfilEditar \n')

		self.kwargs['atualizar_dados'] = True
		return self.kwargs

class UsuarioPerfilEditarEnderecoView(LoginRequiredMixin, TemplateView):
	template_name = 'conta/publico_minha_conta_editar_endereco.html'

	def get_context_data(self, **kwargs):
		print('\n'*20 + '_'*80 + '\n\n VIEW: UsuarioPerfilEditarEndereco \n')

		self.kwargs['atualizar_endereco'] = True
		return self.kwargs

class UsuarioPerfilPedidosView(LoginRequiredMixin, TemplateView):
	template_name =  'conta/publico_meus_pedidos.html'

	def get_context_data(self, **kwargs):
		print('\n'*20 + '_'*80 + '\n\n VIEW: UsuarioPerfilPedidos \n')

		self.kwargs['meus_pedidos'] = True
		return self.kwargs


usuario_cadastro 				= UsuarioCadastroView.as_view()
publico_atualizar_senha			= UsuarioPerfilAtualizarSenhaView.as_view()
usuario_perfil_index 			= UsuarioPerfilIndexView.as_view()
usuario_editar 					= UsuarioPerfilEditarView.as_view()
usuario_perfil_editar_endereco 	= UsuarioPerfilEditarEnderecoView.as_view()
usuario_perfil_pedidos 			= UsuarioPerfilPedidosView.as_view()
