from produto.models import ProdutoCategoria

def navbar_produto(request):
    return {
        'navbar_categorias': ProdutoCategoria.objects.filter(ativo=True)
    }