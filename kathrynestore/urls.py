from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from geral.views import Index, PublicoCategoriaView, PublicoProdutoDetalheView
from usuario.views import UsuarioCadastro

urlpatterns = [
	# DJANGO
	path('admin/', admin.site.urls), path('api-auth/', include('rest_framework.urls')),
	
	# USUÁRIO
	path('accounts/', include('django.contrib.auth.urls')),
	path("accounts/cadastro/", UsuarioCadastro.as_view(), name="signup"),
	
	# PUBLICO
	path('', Index.as_view(), name='index'),
	path('categoria/<slug:slug>/', PublicoCategoriaView.as_view(), name='publico_categoria'),
	path('produto/<slug:slug>/', PublicoProdutoDetalheView.as_view(), name='publico_produto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
