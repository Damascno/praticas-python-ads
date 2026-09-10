estoque = {
    "Arroz": 10,
    "Feijão": 3,
    "Café": 7,
    "Leite": 2,
    "Macarrão": 15
}

for produto, quantidade in estoque.items():
    if quantidade > 5:
        print(f'{produto}: Produto em estoque')
    else:
        print(f'{produto}: Estoque baixo')
