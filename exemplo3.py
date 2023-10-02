# Exemplo 3:
# Solicitar 10 números inteiros ao usuário e contar a quantidade de números pares


cont = 1                    # conta a quantidade de repetições
conta_pares = 0             # conta a quantidade de numeros pares digitadas
while cont <= 10:
    numero = int(input('Numero: '))
    if numero % 2 == 0:
        conta_pares += 1    # conta pares
    cont += 1               # conta repetição

print(f'Quantidade de núneros pares: {conta_pares}')
