"""Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar,
considere US$ 1,0 = R$ 3,27"""
import os
titulo = ' Desafio 010 '
print('{:=^40}'.format(titulo))

real = float(input('\ninforme quantos reais possui na carteira? '))
dolar = real / 3.27
os.system('cls')
print('\nÉ possível comprar {:.3} dólar(es)'.format(dolar))
