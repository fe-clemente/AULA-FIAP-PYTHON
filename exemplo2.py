# SOLICITAR 3 NOTAS E VERIFICAR SE  O ALUNO FOR APROVADO.
# SOLICITAR A QUANTIDADE DE FALTAS
# O ALUNO É APROVADO FOR MAIOR OU IGUAL A 6
# SE A QUANTIDADE DE FALTAS FOR MENOR OU IGUAL A 25

nota1 = float(input("primeira nota:"))
nota2 = float(input("primeira nota:"))
nota3 = float(input("primeira nota:"))

faltas = int(input("quantidade de faltas"))

media = (nota1 + nota2+ nota3) / 3 #(prioridades)

print(f"aluno aprovado: {media >=6 and faltas <=25}")