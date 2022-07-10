from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from carrinho.views import PublicoCarrinho
from geral.views import PublicoIndex, PublicoCategoriaView, PublicoProdutoDetalheView
from usuario.views import UsuarioCadastro

urlpatterns = [
	# DJANGO
	path('admin/', admin.site.urls), path('api-auth/', include('rest_framework.urls')),
	
	# USUÁRIO
	path('accounts/', include('django.contrib.auth.urls')),
	path("accounts/cadastro/", UsuarioCadastro.as_view(), name="signup"),
	
	# PUBLICO
	path('', PublicoIndex.as_view(), name='publico_index'),
	path('categoria/<slug:slug>/', PublicoCategoriaView.as_view(), name='publico_categoria'),
	path('produto/<slug:slug>/', PublicoProdutoDetalheView.as_view(), name='publico_produto'),
	path('carrinho/', login_required(PublicoCarrinho.as_view()), name='publico_carrinho'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
