from model import ProdutoModel
from view import ProdutoView

class ProdutoController:
    def __init__(self):
        self.model = ProdutoModel()
        self.view = ProdutoView(self)
        self.exibir_produtos()  # Mover a chamada para exibir produtos após a inicialização completa da view

    def adicionar_produto(self, nome, marca, quantidade, preco):
        if self.model.verificar_duplicata(nome, marca):
            self.view.exibir_mensagem("Erro", "Já existe um produto com esse nome e marca")
        else:
            self.model.adicionar_produto(nome, marca, quantidade, preco)
            self.view.exibir_mensagem("Sucesso", "Produto adicionado com sucesso!")
            self.view.limpar_campos()
            self.exibir_produtos()

    def exibir_produtos(self):
        produtos = self.model.obter_produtos()
        self.view.mostrar_produtos(produtos)

    def atualizar_produto(self, produto_id, quantidade, preco):
        if quantidade is not None or preco is not None:
            self.model.atualizar_produto(produto_id, quantidade, preco)
            self.view.exibir_mensagem("Sucesso", f"Produto com ID '{produto_id}' atualizado com sucesso")
            self.exibir_produtos()
        else:
            self.view.exibir_mensagem("Erro", "Preencha pelo menos um dos campos de quantidade ou preço")

    def deletar_produto_por_nome(self, nome):
        if self.model.deletar_produto_por_nome(nome):
            self.view.exibir_mensagem("Sucesso", f"Produto '{nome}' deletado com sucesso")
            self.exibir_produtos()
        else:
            self.view.exibir_mensagem("Erro", "Produto não encontrado")

    def deletar_produto_por_id(self, produto_id):
        if self.model.deletar_produto_por_id(produto_id):
            self.view.exibir_mensagem("Sucesso", f"Produto com ID '{produto_id}' deletado com sucesso")
            self.exibir_produtos()
        else:
            self.view.exibir_mensagem("Erro", "Produto não encontrado")

    def pesquisar_por_nome(self, nome):
        produto = self.model.pesquisar_por_nome(nome)
        if produto:
            self.view.mostrar_pesquisa(produto)
        else:
            self.view.exibir_mensagem("Erro", "Produto não encontrado")

    def pesquisar_por_id(self, produto_id):
        produto = self.model.pesquisar_por_id(produto_id)
        if produto:
            self.view.mostrar_pesquisa(produto)
        else:
            self.view.exibir_mensagem("Erro", "Produto não encontrado")

if __name__ == "__main__":
    controller = ProdutoController()
    controller.view.iniciar()
