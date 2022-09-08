import math
n = float(input("Digite um ângulo: "))
ang = math.radians(n)
print(' O ângulo digitado foi: {}° \n Seu seno é: {:.2f} \n Seu cosseno é: {:.2f} \n Sua tangente é {:.2f} '.format(n, math.sin(ang), math.cos(ang), math.tan(ang)))

