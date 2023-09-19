#07 Desenvolva um programa que leia as duas notas de um aluno e calcule e mostre sua média

nota1 = float (input('Digite a nota da sua primeira prova: '))
nota2 = float (input('Digite a nota da sua ultima prova: '))
nf = (nota1 + nota2) / 2

print('Sua Nota final é: {}'.format(nf))
