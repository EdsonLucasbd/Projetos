"""Programa que leia dois numeros e mostre na tela o seu sucessor e antecessor."""
titulo = ' Desafio 05 '
print('{:=^40}'.format(titulo))

num = int(input('\nDigite um número: '))
ant = num - 1
suc = num + 1
print('\nAntecessor: {}\nSucessor: {}'.format(ant, suc))
