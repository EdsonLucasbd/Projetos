print('========== Desafio 4 ==========')
a = input('Digite algo: ')

print('O tipo primitivo é: ', type(a))
print('{} É alfanumerico? {}'.format(a, a.isalnum()))
print('{} É alfabético? {}'.format(a, a.isalpha()))
print('{} Faz parte da tabela ASCII? {}'.format(a, a.isascii()))
print('{} É decimal? {}'.format(a, a.isdecimal()))
print('{} É um dígito? {}'.format(a, a.isdigit()))
print('{} É identificável? {}'. format(a, a.isidentifier()))
print('{} Está em minúsculo? {}'.format(a, a.islower()))
print('{} É maiúsculo? {}'.format(a, a.isupper()))
print('{} É numeral? {}'.format(a, a.isnumeric()))
print('{} É printável? {}'.format(a, a.isprintable()))
print('{} É um espaço? {}'.format(a, a.isspace()))
print('{} É titulo? {}'.format(a, a.istitle()))




