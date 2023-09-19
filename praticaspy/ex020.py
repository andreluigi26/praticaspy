#20 O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
 
from random import shuffle

n1 = str(input('Primeiro Nome: '))
n2 = str(input('Segundo Nome: '))
n3 = str(input('Terceiro Nome: '))
n4 = str(input('Quarto Nome: '))

lista = [n1,n2,n3,n4]
ordem = shuffle(lista)

print("A ordem escohida para apresentação foi:")
print(lista)
