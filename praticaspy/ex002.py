n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2

print('A soma é {} \nÁ multipicação é {} \nE a divisão é {:2f}'.format(s, m, d))
print('A divisão inteira é {} \ne a potência é {}'.format(di, p))