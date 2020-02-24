"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²"""
import os
titulo = ' Desafio 011 '
print('{:=^40}'.format(titulo))

b = float(input('\nInforme a largura (em metros) da parede: '))
h = float(input('\nInforme a altura (em metros) da parede: '))
area = b * h
tinta = area / 2
os.system('cls')
print('\nPrecisa-se de {}L de tinta para pintar todos os {}m² da parede.'.format(tinta, area))
