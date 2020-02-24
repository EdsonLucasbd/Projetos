"""Um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento"""
titulo = ' Desafio 013 '
print('{:=^40}'.format(titulo))

salario = float(input('\nInforme o salário atual: '))
aumento = salario + salario * 0.15
print('\nCom R$ {} de aumento o salário passa a ser de R$ {}'.format((salario * 0.15), aumento))
