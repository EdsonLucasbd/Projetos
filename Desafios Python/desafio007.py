"""Programa que lê duas notas de um aluno calcule a sua media e mostre o resultado"""
titulo = ' Desafio 07 '
print('{:=^40}'.format(titulo))

n1 = int(input('\nInforme a primeira nota: '))
n2 = int(input('\nInforme a segunda nota: '))
media = (n1 + n2) / 2
print('\nA média do aluno é: {}'.format(media))

