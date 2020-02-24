"""Crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada"""
import os
titulo = ' Desafio 06 '
print('{:=^40}'.format(titulo))

num = int(input('\nDigite um número: '))
dob = num * 2
tri = num * 3
raiz = num ** (1/2)
os.system('cls')
print('\nO dobro vale: {}\nO triplo vale: {}\nA raiz quadrada vale: {:.3}'.format(dob, tri, raiz))
