# Sites para consulta de preço e quantidade: https://hortifruti.com.br/catalogsearch/result/?q=Laranja
produtos = {
    'frutas': {
        'Laranja Pera': {'preco/kg': 8.33},
        'Laranja Seleta': {'preco/kg': 11.99},
        'Laranja Lima': {'preco/kg': 10.99},
        'Limão Tahiti': {'preco/kg': 12.99},
        'Limão Siciliano': {'preco/kg': 12.99},
        'Melão': {'preco/kg': 14.99},
        'Banana Prata': {'preco/kg': 9.99},
        'Banana Nanica': {'preco/kg': 11.95},
        'Manga Tommy': {'preco/kg': 9.99},
        'Manga Palmer': {'preco/kg': 19.98},
        'Manga Espada': {'preco/kg': 14.95},
        'Uva Verde': {'preco/kg': 29.98},
        'Uva Preta': {'preco/kg': 25.98},
        'Uva Vermelha': {'preco/kg': 25.98},
        'Abacaxi': {'preco/un': 29.90},
        'Morango': {'preco/kg': 44.98},
    },
    'verduras': {
        'Abóbora': {'preco/kg': 3.00},
        'Abóbora Itália': {'preco/kg': 3.20},
        'Abóbora Japonesa': {'preco/kg': 3.50},
        'Batata doce': {'preco/kg': 2.50},
        'Batata Baroa': {'preco/kg': 3.00},
        'Batata Inglesa': {'preco/kg': 2.20},
        'Beringela': {'preco/kg': 4.50},
        'Beterraba': {'preco/kg': 1.47},
        'Cebola': {'preco/kg': 1.00},
        'Cebola Roxa': {'preco/kg': 2.10},
        'Cenoura': {'preco/kg': 1.12},
        'Chuchu': {'preco/kg': 11.99},
        'Mandioca Embalada': {'preco/kg': 7.79},
        'Pepino': {'preco/kg': 1.75},
        'Pepino Japonês': {'preco/kg': 4.80},
        'Pimentão Amarelo': {'preco/kg': 3.00},
        'Pimentão Verde': {'preco/kg': 5.00},
        'Pimentão Vermelho': {'preco/kg': 4.99},
        'Tomate Carmem': {'preco/kg': 1.40},
        'Tomate Italiano': {'preco/kg': 0.98},
    },
    'folhagens': {
        'Alface Americana': {'preco/un': 4.79},
        'Alface Crespa': {'preco/un': 3.99},
        'Alface Roxa': {'preco/un': 8.29},
        'Alho Nacional': {'preco/un': 2.40},
        'Alho Poró': {'preco/un': 4.95},
        'Agrião': {'preco/un': 4.99},
        'Alecrim': {'preco/un': 4.99},
        'Brócolis Comum': {'preco/un': 12.99},
        'Brócolis Japonês': {'preco/un': 14.99},
        'Cebolinha': {'preco/un': 6.99},
        'Coentro': {'preco/un': 5.99},
        'Couve Manteiga': {'preco/un': 9.99},
        'Rabanete': {'preco/un': 0.60},
        'Rúcula': {'preco/un': 13.99},
    }
}


def get_produtos(categoria=None):
    if categoria:
        return produtos.get(categoria, {})
    return produtos    