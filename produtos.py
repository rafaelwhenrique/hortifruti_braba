import sqlite3

def criar_banco():
    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    entrada.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_tipo TEXT NOT NULL,
        preco_kg REAL NOT NULL,
        kg_ou_unidade TEXT NOT NULL,
        tipo TEXT NOT NULL
        )
    ''')
    banco.commit()
    entrada.close()

# Sites para consulta de preço e quantidade: https://hortifruti.com.br/catalogsearch/result/?q=Laranja
produtos = {
    'frutas': {
        'Laranja Pera': {'preco_kg': 8.33},
        'Laranja Seleta': {'preco_kg': 11.99},
        'Laranja Lima': {'preco_kg': 10.99},
        'Limão Tahiti': {'preco_kg': 12.99},
        'Limão Siciliano': {'preco_kg': 12.99},
        'Melão': {'preco_kg': 14.99},
        'Banana Prata': {'preco_kg': 9.99},
        'Banana Nanica': {'preco_kg': 11.95},
        'Manga Tommy': {'preco_kg': 9.99},
        'Manga Palmer': {'preco_kg': 19.98},
        'Manga Espada': {'preco_kg': 14.95},
        'Uva Verde': {'preco_kg': 29.98},
        'Uva Preta': {'preco_kg': 25.98},
        'Uva Vermelha': {'preco_kg': 25.98},
        'Abacaxi': {'preco_un': 29.90},
        'Morango': {'preco_kg': 44.98},
    },
    'verduras': {
        'Abóbora': {'preco_kg': 3.00},
        'Abóbora Itália': {'preco_kg': 3.20},
        'Abóbora Japonesa': {'preco_kg': 3.50},
        'Batata doce': {'preco_kg': 2.50},
        'Batata Baroa': {'preco_kg': 3.00},
        'Batata Inglesa': {'preco_kg': 2.20},
        'Beringela': {'preco_kg': 4.50},
        'Beterraba': {'preco_kg': 1.47},
        'Cebola': {'preco_kg': 1.00},
        'Cebola Roxa': {'preco_kg': 2.10},
        'Cenoura': {'preco_kg': 1.12},
        'Chuchu': {'preco_kg': 11.99},
        'Mandioca Embalada': {'preco_kg': 7.79},
        'Pepino': {'preco_kg': 1.75},
        'Pepino Japonês': {'preco_kg': 4.80},
        'Pimentão Amarelo': {'preco_kg': 3.00},
        'Pimentão Verde': {'preco_kg': 5.00},
        'Pimentão Vermelho': {'preco_kg': 4.99},
        'Tomate Carmem': {'preco_kg': 1.40},
        'Tomate Italiano': {'preco_kg': 0.98},
    },
    'folhagens': {
        'Alface Americana': {'preco_un': 4.79},
        'Alface Crespa': {'preco_un': 3.99},
        'Alface Roxa': {'preco_un': 8.29},
        'Alho Nacional': {'preco_un': 2.40},
        'Alho Poró': {'preco_un': 4.95},
        'Agrião': {'preco_un': 4.99},
        'Alecrim': {'preco_un': 4.99},
        'Brócolis Comum': {'preco_un': 12.99},
        'Brócolis Japonês': {'preco_un': 14.99},
        'Cebolinha': {'preco_un': 6.99},
        'Coentro': {'preco_un': 5.99},
        'Couve Manteiga': {'preco_un': 9.99},
        'Rabanete': {'preco_un': 0.60},
        'Rúcula': {'preco_un': 13.99},
    }
}

# Cadastrando vários produtos do dicionario produtos de uma vez
def registrar_produtos():
    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    for tipo, chave in produtos.items():
        for nome_tipo, valor_tipo in chave.items():
            preco_kg = list(valor_tipo.values())[0] #pega o preço
            kg_ou_unidade = list(valor_tipo.keys())[0].split('_')[1] #pega se é kg ou un
            entrada.execute('''
                INSERT INTO produtos (nome_tipo, preco_kg, kg_ou_unidade, tipo)
                VALUES (?, ?, ?, ?)
            ''', (nome_tipo, preco_kg, kg_ou_unidade, tipo))
    banco.commit()
    entrada.close()

# def get_produtos(categoria=None):
#     if categoria:
#         return produtos.get(categoria, {})
#     return produtos

if __name__ == '__main__':
    criar_banco()
    registrar_produtos()
    print("Banco de dados criado e produtos inseridos com sucesso!")