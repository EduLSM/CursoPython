cot = float(5.17)
BRL = float(input('Quanto você tem na carteira hoje? '))
USD = BRL/cot
if BRL < 0:
    print('Erro: reinicie e tente novamente com um valor Positivo')

else:
    print('A cotação do USD hoje 22.08.2022 é de R$: {}'.format(cot))
    print('Hoje você poderá comprar U$:{:.2f} com seus R$:{}'.format(USD, BRL))
