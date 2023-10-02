# LISTA - Estrutura de dados que armazena uma sequencia de itens

numeros = [3, 5, 6, 7, 10]

print(numeros)     # exibe a lista
print(numeros[0])  # exibe item da posição 0
print(numeros[1])  # exibe item da posição 1

numeros[0] = 100   # altera item da posição 0
print(numeros)

# len - retorna o tamanho da lista
lista = [9, 4, 0, 2, 12, 1]
print(len(lista))

# sum - retorna o somatório da lista
lista = [9, 4, 0, 2, 12, 1]
print(sum(lista))

# calular a média
media = sum(lista) / len(lista)
print(media)

# sort - ordena a lista
lista = [9, 4, 0, 2, 12, 1]
lista.sort()
print(lista)

# append - insere um item no final da lista
lista = [9, 4, 0, 2, 12, 1]
lista.append(100)
print(lista)

# insert - insere um item em um índice especifico
[9, 4, 0, 2, 12, 1]
lista.insert(0, 100)
print(lista)

# preencher a lista com valores informados pelo usuário
lista = []
for n in range(10):
    numero = int(input('Numero: '))
    lista.append(numero)
print(lista)
