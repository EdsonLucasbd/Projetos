"""Programa que mostra a tabuada de um numero qualquer"""
import os
titulo = ' Desafio 09 '
print('{:=^40}'.format(titulo))

num = int(input('Informe um número: '))
os.system('cls')
print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(num, num, num, num * 2, num, num * 3, num, num * 4, num, num * 5, num, num * 6, num, num * 7, num, num * 8, num, num * 9, num, num * 10))
