import os
titulo = ' CALCULADOR DE IMC '

nome = ''
idade = 0
altura = 0
peso = 0
imc = 0
opcao = 0
while opcao != 4:
    os.system('cls')
    print('{:=^40}'.format(titulo))
    print('''
    1 - Cadastrar
    2 - Calcular IMC
    3 - Mostrar dados
    4 - Sair ''')
    opcao = int(input('\nQual sua opção? '))

    if opcao == 1:
        os.system('cls')
        nome = input('\nOlá, qual o seu nome? ')
        os.system('cls')
        idade = int(input('\nSó por curiosidade {}, qual sua idade? '.format(nome)))
        os.system('cls')
        altura = float(input('\nE qual sua altura? '))
        os.system('cls')
        peso = float(input('\nQual o seu peso atual? '))
        os.system('cls')
    elif opcao == 2:
        imc = peso / altura ** 2
        os.system('cls')
        print('\nIMC = {:.3}'.format(imc))
        if imc < 18.5:
            print('\nVocê está abaixo do peso recomendado, {}\n'.format(nome))
        elif (imc > 18.5) and (imc < 24.9):
            print('\nVocê está com o peso considerado normal {}, parabéns!\n'.format(nome))
        elif (imc > 24.9) and (imc <= 29.9):
            print('\nVocê está com sobrepeso, {}\n'.format(nome))
        elif (imc > 29.9) and (imc <= 34.9):
            print('\nVocê apresenta um quadro de obesidade grau 1, {}\n'.format(nome))
        elif (imc > 34.9) and (imc <= 39.9):
            print('\nVocê apresenta um quadro de obesidade grau 2, {}\n'.format(nome))
        elif imc > 40:
            print('\nVocê apresenta um quadro de obesidade grau 3, {}\n'.format(nome))
        os.system('pause')
    elif opcao == 3:
        os.system('cls')
        print('\nNome: {}\nIdade: {}\nAltura: {:.3}\nPeso: {:.3}'.format(nome, idade, altura, peso))
        os.system('pause')
    elif opcao == 4:
        print('Saindo...')
    else:
        print('\nOpção inválida')
print('\nBy Edson Lucas')

