#17Faça um programa que leia o comprimento do cateto adjacente de um triangulo retangulo, 
# calcule e mostre o seu comprimento da hipoternusa

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipoternusa vai medir {:.2f}'.format(hi))


# Outro jeito

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot (co, ca)
print('A hipoternusa vai medir {:.2f}'.format(hi))