from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from geral.views import publico_index, publico_categoria, publico_produto
from usuario.views import usuario_cadastro

urlpatterns = [
	# DJANGO
	path('admin/', admin.site.urls), path('api-auth/', include('rest_framework.urls')),
	
	# USUÁRIO
	path('accounts/', 				include('django.contrib.auth.urls')),
	path('accounts/cadastro/', 		usuario_cadastro, 						name="signup"),
	path('conta/',					include('usuario.urls')), 

	# PUBLICO
	path('', 						publico_index, 							name='publico_index'),
	path('categoria/<slug:slug>/', 	publico_categoria, 						name='publico_categoria'),
	path('produto/<slug:slug>/', 	publico_produto, 						name='publico_produto'),
	path('carrinho/', 				include('carrinho.urls')),  			# namespace='publico_carrinho'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
