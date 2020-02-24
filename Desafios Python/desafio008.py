"""Programa que leia um valor em metros e o mostre em centimetros e milimetros"""
import os
titulo = ' Desafio 08 '
print('{:=^40}'.format(titulo))

val = float(input('\nDigite um valor em metros: '))
cent = val * 100
mili = val * 1000
os.system('csl')
print('\nValor em centimetros: {}\nValor em milimetros: {}'.format(cent, mili))
