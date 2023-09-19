#18 Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, 
# casseno e tangente desse angulo.

import math

ângulo =  float(input('Digite o valor do ÂNGULO desejado: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O Ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo,cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(ângulo, tangente))