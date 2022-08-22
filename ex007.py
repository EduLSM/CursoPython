nome = input('Qual o nome do aluno(a)')
n1 = float(input('Entre com a primeira nota. '))
n2 = float(input('Entre com a segunda nota. '))
m = (n1 + n2) / 2
print('A média final de {} é {}'.format(nome, m))
# o exercicio só ia até aqui então a partir daqui foi por vontade propria
if m >= 6:
    print('{} está APROVADO(A)'.format(nome))
else:
    print('{} está REPROVADO(A)'.format(nome))
