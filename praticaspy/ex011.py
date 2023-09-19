#11 Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessário para pintá-lo 
#sabendo que cada litro de tinta pinta uma área 2m²

l = int(input('Qual a largura de sua parede? '))
a = int(input('Qual a altura da sua parede? '))
ar = l * a 
tin = ar / 2
print ('Sua área por sua vez tem {}m²'.format(ar))
print ('Você utilizará {} litros de tinta para pintar sua parede'.format(tin))


