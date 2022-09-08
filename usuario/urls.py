from django.urls import path
from django.contrib.auth.decorators import login_required
from usuario.views import usuario_perfil_index, publico_atualizar_senha, usuario_editar, usuario_perfil_editar_endereco, usuario_perfil_pedidos

urlpatterns = [
	path('', 		            	usuario_perfil_index, 					name='publico_minha_conta'),
	path('mudar-senha/', 			publico_atualizar_senha, 				name='publico_minha_conta_atualizar_senha'),
	path('editar-cadastro/', 		usuario_editar, 						name='publico_minha_conta_editar'),
	path('editar-endereco/', 		usuario_perfil_editar_endereco, 		name='publico_minha_conta_editar_endereco'),
	path('meus-pedidos/', 			usuario_perfil_pedidos, 				name='publico_meus_pedidos'),
]