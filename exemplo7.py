# Exemplo 7
# Solicitar 10 números inteiros ao usuário e contar a quantidade de números pares

conta_pares = 0

for n in range(10):
    numero = int(input('Número: '))
    if numero % 2 == 0:
        conta_pares += 1

print(f'Quantidade de números pares: {conta_pares}')
