def forma_pagamento(valor_total):
    
    
    print("\nFormas de pagamento disponíveis:")
    print("1. Crédito")
    print("2. Débito")
    print("3. Dinheiro")
    print("4. Pix")
    
    escolha = input("Escolha a forma de pagamento (1-4): ")
        
    escolha = input("Escolha a forma de pagamento (1-4): ")
        
    if escolha == '1':  # Crédito
        print("Você escolheu pagamento por Crédito.")
        senha = input("Digite a senha do cartão: ")
        print("Processando pagamento...")
        return "Pagamento com crédito aprovado."
        
    elif escolha == '2':  # Débito
        print("Você escolheu pagamento por Débito.")
        senha = input("Digite a senha do cartão: ")
        print("Processando pagamento...")
        return "Pagamento com débito aprovado."
        
    elif escolha == '3':  # Pix
        print("Você escolheu pagamento por Pix.")
        chave_pix = input("Digite sua chave Pix para receber o código de pagamento: ")
        print("Processando pagamento...")
        return "Pagamento por Pix aprovado."
        
    elif escolha == '4':  # Dinheiro
            print("Você escolheu pagamento em Dinheiro.")
            while True:
                try:
                    cedula = float(input("Insira o valor da cédula que possui: R$ "))
                    if cedula >= valor_total:
                        troco = cedula - valor_total
                        print(f"Pagamento aceito. Seu troco é: R$ {troco:.2f}")
                        return "Pagamento em dinheiro concluído."
                    else:
                        print("Valor insuficiente. Por favor, insira uma cédula com valor igual ou superior ao total da compra.")
                except ValueError:
                    print("Valor inválido. Tente novamente inserindo um número.")
        
    else:
        print("Escolha inválida! Por favor, tente novamente.")

# Exemplo de uso:
total_compra = 50.00  # Exemplo de valor total da compra
forma_pagamento(total_compra)
