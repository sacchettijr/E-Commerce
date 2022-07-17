from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, RedirectView
from produto.models import ProdutoCategoria, Produto
from carrinho.models import CarrinhoItem
from django.contrib import messages
from dev_functions import linha_quebra_5  # TODO: apagar em produção


class PublicoCarrinho(TemplateView):
	template_name = 'publico/publico_carrinho.html'
	
	def get_context_data(self, context=None, **kwargs):
		linha_quebra_5()  # TODO: apagar em produção
		self.kwargs['categorias'] = ProdutoCategoria.objects.filter(ativo=True)  # Navbar
		
		self.kwargs['sessao'] = self.request.session
		self.kwargs['sessao_chave'] = self.request.session.session_key
		
		if self.request.user.is_authenticated:
			self.kwargs['usuario'] = self.request.user.email
		else:
			self.kwargs['usuario'] = "Desconhecido"
		
		self.kwargs['carrinho_id'] = 123
		print("\nPRINT >>> CARRINHO_ID: " + str(self.kwargs['carrinho_id']) + "\n\n\n\n")
		
		return self.kwargs


class CreateCarrinhoItemView(RedirectView):
	
	def get_redirect_url(self, *args, **kwargs):
		linha_quebra_5()  # TODO: apagar em produção
		self.kwargs['categorias'] = ProdutoCategoria.objects.filter(ativo=True)  # Navbar
		
		produto = get_object_or_404(Produto, slug=self.kwargs['slug'])
		carrinho_item = CarrinhoItem.objects.add_item(self.request.session.session_key, produto)
		messages.success(self.request, 'Produto adicionado com sucesso.')
		
		return reverse('publico_carrinho', kwargs={produto})
