from django.views.generic import TemplateView


class Index(TemplateView):
	template_name = 'index.html'
	
	def get_context_data(self, context=None, **kwargs):
		self.kwargs['categorias'] = Categoria.objects.filter(
			ativo=True)  # Navbar
		return self.kwargs