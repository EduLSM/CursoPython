import random
n1 = str(input('Nome do aluno: '))
n2 = str(input('Nome do aluno: '))
n3 = str(input('Nome do aluno: '))
n4 = str(input('Nome do aluno: '))
lista = [n1, n2, n3, n4]
esc = random.choice(lista)
print('O o aluno escolhido foi: {}' .format(esc))