h = float(input('Qual a altura da parede em metros? '))
l = float(input('E a largura? '))
a = h*l
ink = a/2
print('A área de sua parede é de {} metros quadrados.'.format(a))
print('Serão precisos, {} litro(s) de tinta para corbir a parade uma vez.'.format(ink))
print('E para duas demãos serão usados', 2*ink,'litros de tinta')