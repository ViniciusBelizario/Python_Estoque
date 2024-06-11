import sqlite3

class ProdutoModel:
    def __init__(self):
        self.conn = sqlite3.connect('estoque.db')
        self.c = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS produtos
                          (id INTEGER PRIMARY KEY, nome TEXT, marca TEXT, quantidade INTEGER, preco REAL)''')
        self.conn.commit()

    def adicionar_produto(self, nome, marca, quantidade, preco):
        self.c.execute("INSERT INTO produtos (nome, marca, quantidade, preco) VALUES (?, ?, ?, ?)", 
                       (nome, marca, int(quantidade), float(preco)))
        self.conn.commit()

    def verificar_duplicata(self, nome, marca):
        self.c.execute("SELECT * FROM produtos WHERE nome=? AND marca=?", (nome, marca))
        return self.c.fetchone() is not None

    def obter_produtos(self):
        self.c.execute("SELECT * FROM produtos")
        return self.c.fetchall()

    def atualizar_produto(self, produto_id, quantidade=None, preco=None):
        if quantidade is not None:
            self.c.execute("UPDATE produtos SET quantidade=? WHERE id=?", (int(quantidade), produto_id))
        if preco is not None:
            self.c.execute("UPDATE produtos SET preco=? WHERE id=?", (float(preco), produto_id))
        self.conn.commit()

    def deletar_produto_por_nome(self, nome):
        self.c.execute("DELETE FROM produtos WHERE nome=?", (nome,))
        self.conn.commit()
        return self.c.rowcount > 0

    def deletar_produto_por_id(self, produto_id):
        self.c.execute("DELETE FROM produtos WHERE id=?", (produto_id,))
        self.conn.commit()
        return self.c.rowcount > 0

    def pesquisar_por_nome(self, nome):
        self.c.execute("SELECT * FROM produtos WHERE nome=?", (nome,))
        return self.c.fetchone()

    def pesquisar_por_id(self, produto_id):
        self.c.execute("SELECT * FROM produtos WHERE id=?", (produto_id,))
        return self.c.fetchone()
