from django.views.generic import TemplateView

from dev_functions import linha_quebra_10
from produto.models import ProdutoCategoria


class PublicoCarrinho(TemplateView):
	template_name = 'publico/publico_carrinho.html'
	
	def get_context_data(self, context=None, **kwargs):
		linha_quebra_10()
		self.kwargs['categorias'] = ProdutoCategoria.objects.filter(ativo=True)  # Navbar
		
		self.kwargs['sessao'] = self.request.session
		print("\n\nPRINT >>> SESSION: " + str(self.kwargs['sessao']))
		
		self.kwargs['sessao_chave'] = self.request.session.session_key
		print("\nPRINT >>> SESSION_KEY: " + str(self.kwargs['sessao_chave']))
		
		if self.request.user.is_authenticated:
			self.kwargs['usuario'] = self.request.user.email
		else:
			self.kwargs['usuario'] = "Desconhecido"
		print("\nPRINT >>> USUÁRIO: " + str(self.kwargs['usuario']))
		
		self.kwargs['carrinho_id'] = 123
		print("\nPRINT >>> CARRINHO_ID: " + str(self.kwargs['carrinho_id']) + "\n\n\n\n")
		
		return self.kwargs
