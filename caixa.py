from produtos import get_produtos
# biblioteca tabulate: https://www.datacamp.com/tutorial/python-tabulate
from tabulate import tabulate #exigir download dessa lib na maquina: pip install --user tabulate
import os
import time

def limpar_tela():
    """Limpa a tela do terminal, compatível com Windows e Unix."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_produtos(produtos):
    for categoria, itens in produtos.items():
        tabela = []
        print(f"\tCategoria: {categoria.capitalize()}")
        for nome, info in itens.items():
            if 'preco/kg' in info:
                preco = info['preco/kg']
                tabela.append([nome, f"R${preco:.2f}/kg"]) 
            elif 'preco/un' in info:
                preco = info['preco/un']
                tabela.append([nome, f"R${preco:.2f}/un"])  
        print(tabulate(tabela, headers = ["Produto", "Preço"], stralign="center",tablefmt="fancy_grid"))

# def mostrar_produtos(produtos):
#     for categoria, itens in produtos.items():
#         print(f"\nCategoria: {categoria.capitalize()}")
#         for nome, info in itens.items():
#             if 'preco/kg' in info:
#                 preco = info['preco/kg']
#                 print(f"Produto: {nome}, Preço: R${preco:.2f}/kg")
#             elif 'preco/un' in info:
#                 preco = info['preco/un']
#                 print(f"Produto: {nome}, Preço: R${preco:.2f}/un")


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
        
def realizar_compra(produtos):
    total = 0.0
    itens_comprados = []

    while True:
        categoria = input("\nEscolha uma categoria de produtos (frutas, verduras, folhagens) ou digite 'sair' para finalizar a compra: ").lower()
        if categoria == 'sair':
            break

        if categoria in produtos:
            limpar_tela()
            mostrar_produtos({categoria: produtos[categoria]})

            produto_escolhido = input("\nDigite o nome do produto que deseja comprar ou 'voltar' para escolher outra categoria: ").title()

            if produto_escolhido == 'voltar':
                continue

            if produto_escolhido in produtos[categoria]:
                if categoria in ['frutas', 'verduras']:
                    quantidade = float(input(f"Quantos kg você deseja comprar? (ex: 0.5 para 500g, 1.0 para 1kg): "))
                    preco_produto = produtos[categoria][produto_escolhido]['preco/kg']
                    subtotal = preco_produto * quantidade
                    print(f"{quantidade} - {produto_escolhido}(s) adicionado(s) ao carrinho. Subtotal: R${subtotal:.2f}")

                elif categoria == 'folhagens':
                    quantidade = int(input(f"Quantas unidades você deseja comprar? (ex: 1 para 1 unidade): "))
                    preco_produto = produtos[categoria][produto_escolhido]['preco/un']
                    subtotal = preco_produto * quantidade
                    print(f"{quantidade} unidade(s) {produto_escolhido}(s) adicionado(s) ao carrinho. Subtotal: R${subtotal:.2f}")
                
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
    produtos = get_produtos()
    total, itens_comprados = realizar_compra(produtos)
    finalizar_compra(total, itens_comprados)

if __name__ == "__main__":
    sistema_caixa()