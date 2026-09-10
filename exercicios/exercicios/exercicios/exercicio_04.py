carrinho = [
    ("Arroz", 2, 25.00),
    ("Feijão", 1, 8.00),
    ("Café", 3, 15.00),
    ("Leite", 2, 6.00)
]

total_compra = 0

for produto, quantidade, preco in carrinho:
    total = quantidade * preco
    total_compra += total

    print(f'{produto}: R$ {total:.2f}')

print(f'Total da compra: R$ {total_compra:.2f}')
