"""Um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto"""
titulo = ' Desafio 012 '
print('{:=^40}'.format(titulo))

preco = float(input('\nQual o preço do produto? '))
desconto = preco - preco * 0.05
print('\nO valor com desconto é: R$ {:.3}.'.format(desconto))
