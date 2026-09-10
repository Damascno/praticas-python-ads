compras = [
    ("Arroz", 2, 25.00),
    ("Feijão", 3, 8.00),
    ("Café", 2, 15.00),
    ("Leite", 5, 6.00)
]

for produto, quantidade, preco in compras:
    total = quantidade * preco

    if total >= 50:
        desconto = total * 0.10
        total_final = total - desconto

        print(f'{produto}: R$ {total:.2f}')
        print('10% de desconto!')
        print(f'Valor final: R$ {total_final:.2f}\n')
    else:
        print(f'{produto}: R$ {total:.2f}')
        print('Sem desconto.\n')
