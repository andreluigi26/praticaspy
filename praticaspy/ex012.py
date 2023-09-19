#12 Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto 

prod = float(input('Digite o valor de prateleira do produto: R$'))
desc = prod * 0.05
#vf = prod - desc
print('Parabéns, você ganhou 5% desconto e o valor da compra ficou R${}'.format(prod - desc))