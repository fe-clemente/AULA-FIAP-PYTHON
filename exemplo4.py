# Exemplo 4:
# Solicitar 10 números inteiros ao usuário e calcular a média aritmética dos números

cont = 1            # contadora
soma = 0            # somadora
while cont <= 10:
    numero = int(input('Numero: '))
    soma += numero
    cont += 1

print(f'Somatório dos números: {soma}')

media = soma / 10
print(f'Média dos números: {media}')
