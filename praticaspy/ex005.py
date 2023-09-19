#05 Faça um progrma que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número: '))
n2 = n1 + 1
n3 = n1 - 1
print('O número digitado foi {} \nO seu sucessor é {} \nE o seu antecessor é {}'.format(n1, n2, n3))

#Outro modo para fazer

n = int(input('Dugute um número: '))
print('Analisando o valor {} \nO seu sucessor é {} \nE o seu antecessor é {}'.format(n, (n+1), (n-1)))