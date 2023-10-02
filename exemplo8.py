

quantidade = int(input('Informa a quantidade de alunos: '))

soma = 0
for n in range(1, quantidade+1, 2):
    nota = float(input(f'Nota do aluno {n}: '))
    soma += nota

media = soma / (quantidade / 2)
print(f'Média dos alunos ímpares: {media}')


soma = 0
for n in range(2, quantidade+1, 2):
    nota = float(input(f'Nota do aluno {n}: '))
    soma += nota

media = soma / (quantidade / 2)
print(f'Média dos alunos pares: {media}')
