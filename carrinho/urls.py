from django.contrib.auth.decorators import login_required
from django.urls import path
from carrinho.views import publico_carrinho, publico_carrinho_item


urlpatterns = [
	path('', 						login_required(publico_carrinho), 			name='publico_carrinho'),
	path('adicionar/<slug:slug>', 	login_required(publico_carrinho_item), 		name='publico_create_carrinho_item')
]
