from turtle import clear
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.forms import modelformset_factory
from django.views.generic import TemplateView, RedirectView
from produto.models import ProdutoCategoria, Produto, ProdutoImagem
from carrinho.models import CarrinhoItem
from django.contrib import messages


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
			formset = CarrinhoItemFormSet(
				queryset=CarrinhoItem.objects.none()
			)
		return formset
	
	def get_context_data(self, **kwargs):
		print('\n'*20 + '_'*80 + '\n\n VIEW: PublicoCarrinhoView')
		context = super(PublicoCarrinhoView, self).get_context_data(**kwargs)
		context['formset'] = self.get_formset()
		context['produtos_imagens'] = ProdutoImagem.objects.filter(padrao=True)

		# Verifica se possui algum item já adicionado
		if context['formset'].queryset:
			context['existe_item'] = True
		else:
			context['existe_item'] = False
		
		print('\n\n')
		print('PRINT >>> EXISTE ITEM NO CARRINHO? - {}'.format(context['existe_item']))
		contador = 0
		for item in context['formset'].queryset:
			contador = contador + 1
			print('PRINT >>> ITEM DO CARRINHO {} - Produto ({})'.format(contador, item.pk))
		# print('\nPRINT >>> ' + str(context['produtos_imagens']))
		print('\n\n')

		return context
	
	def post(self, request, *args, **kwargs):
		formset = self.get_formset()
		context = self.get_context_data(**kwargs)
		
		if formset.is_valid():
			formset.save()
			messages.success(request, 'Carrinho atualizado com sucesso.')
			context['formset'] = self.get_formset(clear=True)
			
			# Verifica se possui algum item já adicionado
			if context['formset'].queryset:
				context['existe_item'] = True
			else:
				context['existe_item'] = False
		
		return self.render_to_response(context)


class CreateCarrinhoItemView(RedirectView):
	
	def get_redirect_url(self, *args, **kwargs):		
		print('\n'*20 + '_'*80 + '\n\n VIEW: CreateCarrinhoItemView')
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
