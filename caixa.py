# biblioteca tabulate: https://www.datacamp.com/tutorial/python-tabulate
from tabulate import tabulate #exigir download dessa lib na maquina: pip install tabulate
import sqlite3
import os
import time

def limpar_tela():
    """Limpa a tela do terminal, compatível com Windows e Unix."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def conectar_banco():
    return sqlite3.connect('hortifruti.db')

def mostrar_produtos():
    conexao = sqlite3.connect('hortifruti.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT DISTINCT tipo FROM produtos")
    tipos = cursor.fetchall()
    for tipo in tipos:
        tipo_nome = tipo[0]
        print(f"\nCategoria: {tipo_nome.capitalize()}")
        
        cursor.execute("SELECT nome_tipo, preco_kg, kg_ou_unidade FROM produtos WHERE tipo = ?", (tipo_nome,))
        produtos = cursor.fetchall()
        
        tabela = [[nome, f"R${preco:.2f}/{unidade}"] for nome, preco, unidade in produtos]
        print(tabulate(tabela, headers=["Produto", "Preço"], stralign="center", tablefmt="fancy_grid"))
    
    conexao.close()


def forma_pagamento():
    """Solicita ao usuário a forma de pagamento escolhida."""
    print("\nFormas de pagamento disponíveis:")
    print("1. Crédito")
    print("2. Débito")
    print("3. Dinheiro")
    print("4. Pix")
    
    escolha = input("Escolha a forma de pagamento (1-4): ")
    
    if escolha == '1':
        return "Crédito"
    elif escolha == '2':
        return "Débito"
    elif escolha == '3':
        return "Dinheiro"
    elif escolha == '4':
        return "Pix"
    else:
        print("Escolha inválida! Tente novamente.")
        return forma_pagamento()

def cadastrar_usuario():
    """Verifica se o usuário possui cadastro na loja."""
    cadastro = input("Você já possui cadastro na loja? (s/n): ").lower()
    
    if cadastro == 's':
        cpf = input("Por favor, insira o seu CPF (ex: 02340521790): ")
        print(f"CPF {cpf} verificado!")
    elif cadastro == 'n':
        sugerir_cadastro = input("Deseja fazer um cadastro? (s/n): ").lower()
        if sugerir_cadastro == 's':
            cpf = input("Por favor, insira o seu CPF (ex: 02340521790): ")
            print(f"Número de cpf cadastrado com sucesso!")
        elif sugerir_cadastro == 'n':
            print("Continuando sem cadastro...")
        else: 
            print("Continuando sem cadastro...")
    else: 
        print("Continuando sem cadastro...")
        
def realizar_compra():
    conexao = sqlite3.connect('hortifruti.db')
    cursor = conexao.cursor()
    total = 0.0
    itens_comprados = []

    while True:
        cursor.execute("SELECT DISTINCT tipo FROM produtos")
        categorias = [tipo[0] for tipo in cursor.fetchall()]
        print("\nCategorias disponíveis:", ", ".join(categorias))

        categoria = input("\nEscolha uma categoria de produtos (frutas, verduras, folhagens) ou digite 'sair' para finalizar a compra: ").lower()
        if categoria == 'sair':
            break

        if categoria in categorias:
            cursor.execute("SELECT nome_tipo, preco_kg, kg_ou_unidade FROM produtos WHERE tipo = ?", (categoria,))
            produtos = cursor.fetchall()
            print(f"\nProdutos da categoria {categoria.capitalize()}:")
            for produto in produtos:
                nome, preco, unidade = produto
                print(f"{nome} - R${preco:.2f}/{unidade}")

            produto_escolhido = input("\nDigite o nome do produto que deseja comprar ou 'voltar' para escolher outra categoria: ").title()
            if produto_escolhido == 'voltar':
                continue
            cursor.execute("SELECT preco_kg, kg_ou_unidade FROM produtos WHERE nome_tipo = ? AND tipo = ?", (produto_escolhido, categoria))
            resultado = cursor.fetchone()
            if resultado:
                preco_produto, unidade = resultado
                if unidade == 'kg':
                    quantidade = float(input("Quantos kg deseja comprar? "))
                    subtotal = preco_produto * quantidade
                    print(f"{quantidade} kg de {produto_escolhido} adicionado(s) ao carrinho. Subtotal: R${subtotal:.2f}")
                else:
                    quantidade = int(input("Quantas unidades deseja comprar? "))
                    subtotal = preco_produto * quantidade
                    print(f"{quantidade} unidade(s) de {produto_escolhido} adicionada(s) ao carrinho. Subtotal: R${subtotal:.2f}")

                total += subtotal
                itens_comprados.append((produto_escolhido, quantidade, subtotal))
            else:
                print("Produto não encontrado. Tente novamente.")
        else:
            print("Categoria inválida. Tente novamente.")

    return total, itens_comprados

def finalizar_compra(total, itens_comprados):
    """Finaliza a compra, mostrando o resumo e o total a pagar."""
    if itens_comprados:
        print("\nResumo da Compra:")
        for item in itens_comprados:
            print(f"{item[1]} de {item[0]} - Subtotal: R${item[2]:.2f}")
        print(f"\nTotal a pagar: R${total:.2f}")

        pagamento = forma_pagamento()
        print(f"Forma de pagamento escolhida: {pagamento}")
        print("Pagamento realizado com sucesso! Obrigado pela sua compra.")
    else:
        print("Nenhum item foi comprado.")

def sistema_caixa():
    """Executa o sistema de caixa do hortifruti."""
    limpar_tela()
    print("Bem-vindo ao sistema de caixa do hortifruti!")
    time.sleep(1.5)
    cadastrar_usuario()
    print("Te redirecionando para o nosso catálogo...")
    time.sleep(1.5)
    total, itens_comprados = realizar_compra()
    finalizar_compra(total, itens_comprados)

if __name__ == "__main__":
    sistema_caixa()