# Exemplo 5:
# Implementar uma calculadora com as operações de soma, subtração, multiplicação e divisão

while True:
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')
    opcao = int(input('Escolha uma opção: '))

    if 1 <= opcao <= 4:
        a = float(input('Primeiro numero: '))
        b = float(input('Segundo numero: '))

    if opcao == 1:
        print(f'Resultado da soma: {a + b}')
    elif opcao == 2:
        print(f'Resultado da subtração: {a - b}')
    elif opcao == 3:
        print(f'Resultado da multiplicação: {a * b}')
    elif opcao == 4:
        print(f'Resultado da divisão: {a / b}')
    elif opcao == 5:
        print('Programa Encerrado')
        break
    else:
        print('ERRO. Opção inválida')
