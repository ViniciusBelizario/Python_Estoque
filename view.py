import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd

class ProdutoView:
    def __init__(self, controller):
        self.controller = controller
        self.janela = tk.Tk()
        self.janela.title("Minha Empresa de Estoque - Controle de Estoque")

        # Menu
        self.menu_bar = tk.Menu(self.janela)
        self.janela.config(menu=self.menu_bar)

        # Menu Relatório
        self.relatorio_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Relatórios", menu=self.relatorio_menu)
        self.relatorio_menu.add_command(label="Gerar Relatório", command=self.gerar_relatorio)
        self.relatorio_menu.add_command(label="Salvar como CSV", command=lambda: self.salvar_relatorio('csv'))
        self.relatorio_menu.add_command(label="Salvar como XLSX", command=lambda: self.salvar_relatorio('xlsx'))
        self.relatorio_menu.add_command(label="Salvar como TXT", command=lambda: self.salvar_relatorio('txt'))

        # Menu Pesquisa
        self.pesquisa_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Pesquisar Produto", menu=self.pesquisa_menu)
        self.pesquisa_menu.add_command(label="Abrir Pesquisa", command=self.abrir_janela_pesquisa)

        # Menu Exclusão
        self.exclusao_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Excluir Produto", menu=self.exclusao_menu)
        self.exclusao_menu.add_command(label="Abrir Exclusão", command=self.abrir_janela_exclusao)

        # Menu Atualização
        self.atualizacao_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Atualizar Produto", menu=self.atualizacao_menu)
        self.atualizacao_menu.add_command(label="Abrir Atualização", command=self.abrir_janela_atualizacao)

        # Título
        self.titulo = tk.Label(self.janela, text="Minha Empresa de Estoque - Controle de Estoque", font=("Arial", 16))
        self.titulo.pack(pady=10)

        # Campos de entrada de texto
        tk.Label(self.janela, text="Nome do Produto").pack()
        self.entrada_nome = tk.Entry(self.janela, font=("Arial", 12))
        self.entrada_nome.pack(pady=5)

        tk.Label(self.janela, text="Marca do Produto").pack()
        self.entrada_marca = tk.Entry(self.janela, font=("Arial", 12))
        self.entrada_marca.pack(pady=5)

        tk.Label(self.janela, text="Quantidade").pack()
        self.entrada_quantidade = tk.Entry(self.janela, font=("Arial", 12))
        self.entrada_quantidade.pack(pady=5)

        tk.Label(self.janela, text="Preço").pack()
        self.entrada_preco = tk.Entry(self.janela, font=("Arial", 12))
        self.entrada_preco.pack(pady=5)

        # Botão para adicionar produto
        self.botao_adicionar = tk.Button(self.janela, text="Adicionar Produto", command=self.adicionar_produto, font=("Arial", 12))
        self.botao_adicionar.pack(pady=10)

        # Frame para exibir produtos
        self.frame_produtos = tk.Frame(self.janela)
        self.frame_produtos.pack(pady=10)

    def iniciar(self):
        self.janela.mainloop()

    def adicionar_produto(self):
        nome = self.entrada_nome.get()
        marca = self.entrada_marca.get()
        quantidade = self.entrada_quantidade.get()
        preco = self.entrada_preco.get()
        self.controller.adicionar_produto(nome, marca, quantidade, preco)

    def atualizar_produto(self):
        produto_id = self.entrada_atualizar_id.get()
        quantidade = self.entrada_atualizar_quantidade.get()
        preco = self.entrada_atualizar_preco.get()
        self.controller.atualizar_produto(produto_id, quantidade, preco)
        self.janela_atualizacao.destroy()  # Fechar a janela de atualização

    def mostrar_produtos(self, produtos):
        for widget in self.frame_produtos.winfo_children():
            widget.destroy()

        for produto in produtos:
            tk.Label(self.frame_produtos, text=f"ID: {produto[0]} | Nome: {produto[1]} | Marca: {produto[2]} | Quantidade: {produto[3]} | Preço: {produto[4]}").pack()

    def mostrar_pesquisa(self, produto):
        messagebox.showinfo("Resultado da Pesquisa", f"ID: {produto[0]}\nNome: {produto[1]}\nMarca: {produto[2]}\nQuantidade: {produto[3]}\nPreço: {produto[4]}")

    def exibir_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    def limpar_campos(self):
        self.entrada_nome.delete(0, tk.END)
        self.entrada_marca.delete(0, tk.END)
        self.entrada_quantidade.delete(0, tk.END)
        self.entrada_preco.delete(0, tk.END)

    def abrir_janela_pesquisa(self):
        janela_pesquisa = tk.Toplevel(self.janela)
        janela_pesquisa.title("Pesquisar Produto")

        tk.Label(janela_pesquisa, text="Pesquisar por Nome").pack()
        self.entrada_pesquisa_nome = tk.Entry(janela_pesquisa, font=("Arial", 12))
        self.entrada_pesquisa_nome.pack(pady=5)
        botao_pesquisar_nome = tk.Button(janela_pesquisa, text="Pesquisar por Nome", command=self.pesquisar_por_nome, font=("Arial", 12))
        botao_pesquisar_nome.pack(pady=5)

        tk.Label(janela_pesquisa, text="Pesquisar por ID").pack()
        self.entrada_pesquisa_id = tk.Entry(janela_pesquisa, font=("Arial", 12))
        self.entrada_pesquisa_id.pack(pady=5)
        botao_pesquisar_id = tk.Button(janela_pesquisa, text="Pesquisar por ID", command=self.pesquisar_por_id, font=("Arial", 12))
        botao_pesquisar_id.pack(pady=5)

    def abrir_janela_exclusao(self):
        self.janela_exclusao = tk.Toplevel(self.janela)
        self.janela_exclusao.title("Excluir Produto")

        tk.Label(self.janela_exclusao, text="Excluir por Nome").pack()
        self.entrada_deletar_nome = tk.Entry(self.janela_exclusao, font=("Arial", 12))
        self.entrada_deletar_nome.pack(pady=5)
        botao_deletar_nome = tk.Button(self.janela_exclusao, text="Excluir por Nome", command=self.deletar_por_nome, font=("Arial", 12))
        botao_deletar_nome.pack(pady=5)

        tk.Label(self.janela_exclusao, text="Excluir por ID").pack()
        self.entrada_deletar_id = tk.Entry(self.janela_exclusao, font=("Arial", 12))
        self.entrada_deletar_id.pack(pady=5)
        botao_deletar_id = tk.Button(self.janela_exclusao, text="Excluir por ID", command=self.deletar_por_id, font=("Arial", 12))
        botao_deletar_id.pack(pady=5)

    def abrir_janela_atualizacao(self):
        self.janela_atualizacao = tk.Toplevel(self.janela)
        self.janela_atualizacao.title("Atualizar Produto")

        tk.Label(self.janela_atualizacao, text="ID do Produto").pack()
        self.entrada_atualizar_id = tk.Entry(self.janela_atualizacao, font=("Arial", 12))
        self.entrada_atualizar_id.pack(pady=5)

        tk.Label(self.janela_atualizacao, text="Nova Quantidade").pack()
        self.entrada_atualizar_quantidade = tk.Entry(self.janela_atualizacao, font=("Arial", 12))
        self.entrada_atualizar_quantidade.pack(pady=5)

        tk.Label(self.janela_atualizacao, text="Novo Preço").pack()
        self.entrada_atualizar_preco = tk.Entry(self.janela_atualizacao, font=("Arial", 12))
        self.entrada_atualizar_preco.pack(pady=5)

        botao_atualizar = tk.Button(self.janela_atualizacao, text="Atualizar Produto", command=self.atualizar_produto, font=("Arial", 12))
        botao_atualizar.pack(pady=10)

    def pesquisar_por_nome(self):
        nome = self.entrada_pesquisa_nome.get()
        self.controller.pesquisar_por_nome(nome)

    def pesquisar_por_id(self):
        produto_id = self.entrada_pesquisa_id.get()
        self.controller.pesquisar_por_id(produto_id)

    def deletar_por_nome(self):
        nome = self.entrada_deletar_nome.get()
        self.controller.deletar_produto_por_nome(nome)
        self.janela_exclusao.destroy()  # Fechar a janela de exclusão

    def deletar_por_id(self):
        produto_id = self.entrada_deletar_id.get()
        self.controller.deletar_produto_por_id(produto_id)
        self.janela_exclusao.destroy()  # Fechar a janela de exclusão

    def gerar_relatorio(self):
        relatorio = tk.Toplevel(self.janela)
        relatorio.title("Relatório de Produtos")
        
        produtos = self.controller.model.obter_produtos()
        
        for produto in produtos:
            tk.Label(relatorio, text=f"ID: {produto[0]} | Nome: {produto[1]} | Marca: {produto[2]} | Quantidade: {produto[3]} | Preço: {produto[4]}").pack()

    def salvar_relatorio(self, formato):
        produtos = self.controller.model.obter_produtos()
        df = pd.DataFrame(produtos, columns=["ID", "Nome", "Marca", "Quantidade", "Preço"])

        file_path = filedialog.asksaveasfilename(defaultextension=f".{formato}", filetypes=[(f"{formato.upper()} files", f"*.{formato}"), ("All files", "*.*")])
        if file_path:
            if formato == 'csv':
                df.to_csv(file_path, index=False)
            elif formato == 'xlsx':
                df.to_excel(file_path, index=False)
            elif formato == 'txt':
                df.to_csv(file_path, index=False, sep='\t')
            self.exibir_mensagem("Sucesso", f"Relatório salvo como {formato.upper()} com sucesso!")
