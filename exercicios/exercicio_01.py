alunos = [
    ("Alice", 8),
    ("Bob", 5),
    ("Carol", 9),
    ("David", 6),
    ("Eve", 4)
]

for aluno, nota in alunos:
    if nota >= 7:
        print(f'{aluno}: Aprovado')
    elif nota >= 5:
        print(f'{aluno}: Recuperação')
    else:
        print(f'{aluno}: Reprovado')
