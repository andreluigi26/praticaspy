#06 Crie um algoritimo que leia um número e mostre o seu dobro e o triplo e raiz quadrada

n1 = int(input('Digite um valor qualquer: '))
n2 = n1 * 2
n3 = n1 * 3
n4 = n1 ** (1/2)

print('O valor digitado foi {} \nO dobro de {} é {} \nE o triplo é {} \nA raiz quadrada de {} é {:2f}'.format(n1,n1,n2,n3,n1,n4))