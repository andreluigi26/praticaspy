#13 Faça um algoritimo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento

sl = float(input('Digite o seu sálario: R$'))
slf = sl * 0.15
print ('Parabéns, você foi promovido! O seu novo sálario é de: R${}'.format(sl + slf))