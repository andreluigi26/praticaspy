#10 Crie um programa que leia o quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares 
#ela pode comprar (CONSIDERE US 1,00$ = 3,27R$)

r = float(input('Quanto você tem na sua carteira agora? R$'))
d = r / 4.87
print('Com R${:.2f}, Você teria US${:.2f} dolares'.format(r,d))