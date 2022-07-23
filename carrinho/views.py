from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.forms import modelformset_factory
from django.views.generic import TemplateView, RedirectView
from produto.models import ProdutoCategoria, Produto
from carrinho.models import CarrinhoItem
from django.contrib import messages
from dev_functions import linha_quebra_5  # TODO: apagar em produção


class PublicoCarrinhoView(TemplateView):
	template_name = 'publico/publico_carrinho.html'
	
	def get_formset(self, clear=False):
		
		CarrinhoItemFormSet = modelformset_factory(
			CarrinhoItem, fields=('quantidade',), can_delete=True, extra=0
		)
		
		chave_sessao = self.request.session.session_key
		
		if chave_sessao:
			if clear:
				formset = CarrinhoItemFormSet(
					queryset=CarrinhoItem.objects.filter(chave_carrinho=chave_sessao)
				)
			else:
				formset = CarrinhoItemFormSet(
					queryset=CarrinhoItem.objects.filter(chave_carrinho=chave_sessao),
					data=self.request.POST or None
				)
		else:
			formset = CarrinhoItemFormSet(queryset=CarrinhoItem.objects.none())
		
		return formset
	
	def get_context_data(self, context=None, **kwargs):
		context = super(PublicoCarrinhoView, self).get_context_data(**kwargs)
		context['formset'] = self.get_formset()
		
		return context
	
	def post(self, request, *args, **kwargs):
		formset = self.get_formset()
		context = self.get_context_data(**kwargs)
		
		if formset.is_valid():
			formset.save()
			messages.success(request, 'Carrinho atualizado com sucesso.')
			context['formset'] = self.get_formset(clear=True)
		
		return self.render_to_response(context)


class CreateCarrinhoItemView(RedirectView):
	
	def get_redirect_url(self, *args, **kwargs):		
		produto = get_object_or_404(Produto, slug=self.kwargs['slug'])
		
		if self.request.session.session_key is None:
			self.request.session.save()
		
		carrinho_item, created = CarrinhoItem.objects.add_item(
			self.request.session.session_key, produto
		)
		
		if created:
			messages.success(self.request, 'Produto adicionado com sucesso.')
		else:
			messages.success(self.request, 'Produto atualizado com sucesso.')
		
		return reverse('publico_carrinho')
