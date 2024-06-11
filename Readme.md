# Controle de Estoque

Este é um aplicativo de controle de estoque desenvolvido em Python utilizando o padrão de projeto MVC (Model-View-Controller). A aplicação permite adicionar, atualizar, excluir e pesquisar produtos, além de gerar relatórios em diferentes formatos.

## Funcionalidades

- Adicionar produto
- Atualizar produto
- Excluir produto
- Pesquisar produto por nome ou ID
- Gerar relatórios em formatos CSV, XLSX e TXT

## Estrutura do Projeto

- `model.py`: Contém a lógica de interação com o banco de dados.
- `controller.py`: Contém a lógica de controle, fazendo a ponte entre a visão e o modelo.
- `view.py`: Contém a lógica da interface gráfica.
- `app.py`: Arquivo principal para executar a aplicação.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório para sua máquina local:
    ```sh
    git clone https://github.com/ViniciusBelizario/Python_Estoque.git
    ```
3. Navegue até o diretório do projeto:
    ```sh
    cd seu-repositorio
    ```
4. Instale as dependências necessárias a partir do arquivo `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```
5. Execute a aplicação:
    ```sh
    python app.py
    ```

## Estrutura de Arquivos

```plaintext
.
├── app.py
├── controller.py
├── model.py
├── view.py
└── requirements.txt
