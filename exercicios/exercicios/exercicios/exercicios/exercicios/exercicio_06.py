def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


nota1 = 8
nota2 = 7
nota3 = 9

media = calcular_media(nota1, nota2, nota3)

print(f"Média: {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
