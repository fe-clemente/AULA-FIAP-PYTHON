# OPERADORES ARITIMETICOS
x = 10
y = 30
soma = x + y + 3 - 10
print(soma)

print(3 + 5)  # adicao
print(10 - 4)  # subtração
print(10 * 4)  # multiplicao
print(10 / 4)  # divisao
print(10 // 4)  # divisao inteiro
print(10 % 4)  # restro divisao inteira
print(10 * 2)  # potencia

"""""
# ENTRADA DE DADOS (input)
nome = input("informe seu nome: ")
idade =int(input("Infome sua idade: "))
#int para retornar texto em numero
altura =float(input( "informe seu peso:"))
# flot para retornar a numero quebrado

#PORCENTAGEM
valor= 100
porcentagem = valor * 5 / 100
print(valor)

#SAIDA DE DADOS
print(nome, idade, altura)
print ("O seu nome é {} e sua idade é {}".format(nome, idade))
print (f"O seu nome é {nome} e sua idade é {idade}")
"""

# OPERADORES RELACIONAIS (comparacao entre valores)
numero = 10
print(numero == 10)  # igualdade
print(numero != 10)  # diferente
print(numero <20)   # menor
print(numero >20)    # maior
print(numero <=20)   #menos ou igual
print(numero >=20)  #maior ou igual

idade =int(input("informe sua idade: "))
print(f"Maior de idade: {idade >=18}")  #comparacao

#operador in (compracao, ver se uma palavra ou letra esta dentro do texto, retorna verdadeiro ou falso)
texto = input("Digite um texto:")
print("x" in texto.lower()) #CONVERTE EM MINUSCULO
print("x" in texto.upper()) #CONVERTE EM MAIUSCULO

nome = input("digite seu nome: ")
print(nome.title())  # coloca as incial em maiusculo
print(nome.capitalize())  #Coloca a primeira letra em maiculo

#Operadores Logicos
idade=int(input("Informe sua idade"))
print(idade >18 and idade <50) #faz comparacoes as duas devem ser verdadeiras

#doar sangue
#and
idade =  int(input("qual sua idade"))
print(f'pode doar sangue? {idade>=16 and <=69}')
# as duas devem ser verdadeiras com and

# OR
#qualquer uma das duas pode ser verdadeira para que o resultado final seja verdadeiro

media= float(input( "informe a media do aluno"))
faltas= int(input( "informe a quantidade de faltas"))
print(f"o aluno foi reprovado? {media < 6 or faltas > 25}")


#not - inverte o falso com verdadeiro e o verdadeiro com falso
#a pessoa é maior de idade se a pessoa for maior ou igual a 18 anos

idade=int(input(" informe a sua idade: ?"))
print(f" é maior de idade " {not idade <18})

if idade >=18:  #é executado se a condicao for verdadeira
    print(f" a pessoa  é maior de idade")
else:
    print("A pessoa é menor de idade")# é executado se a condicao for falsa