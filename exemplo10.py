# Preencher a lista com nomes de 10 pessoas e realizar a busca por um nome especifico

# preencher a lista
lista = []
for i in range(10):
    nome = input('Nome: ')
    lista.append(nome)
print(lista)

nome = input('Digite um nome para procurar na lista: ')

cont = 0
# percorre itens da lista
for item in lista:
    if item == nome:
        cont += 1

if cont == 0:
    print(f'Nome não encontrado {cont} vezes')
else:
    print('Nome encontrado')
