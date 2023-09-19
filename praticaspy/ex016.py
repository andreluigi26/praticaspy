#16 Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
#EX: Digite um número: 6.127 | O numero 6.127 tem a parte inteira 6

import math

num = float(input('Digite um número qualquer: '))
por = math.floor(num)
print('O numero {} tem a parte inteira de {}'.format(num, por))


# Correção

from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado {} e sua porção inteira é {}'.format(num, trunc(num)))