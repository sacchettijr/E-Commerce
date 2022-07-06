from django.views.generic import TemplateView

from produto.models import ProdutoCategoria


# VIEWS PUBLICAS
class Index(TemplateView):
	template_name = 'publico/index.html'
	
	def get_context_data(self, context=None, **kwargs):
		self.kwargs['categorias'] = ProdutoCategoria.objects.filter(
			ativo=True)  # Navbar
		return self.kwargs

# VIEWS DE GERAL
