
# importação de módulos
from math import sqrt           # módulo do python
from meumodulo import somar, multiplicar  # mpodulo criado no projeto


numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

c = somar(numero1, numero2)
print(f'Resultado da soma: {c}')

c = multiplicar(numero1, numero2)
print(f'Resultado da soma: {c}')

n = sqrt(10)
print(f'Raiz quadrada de 10 é {n}')
