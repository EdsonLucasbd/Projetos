import MySQLdb
# Criar conexão com o servidor
conexao = MySQLdb.connect('localhost', 'root', '123456')
conexao.select_db('cactusdb')

cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS `cactusdb`.`usuarios` (
  `Nome` VARCHAR(255) NOT NULL,
  `Email` VARCHAR(255) NOT NULL,
  `Senha` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Email`));
''')
print('\nConectado com o Banco de dados\n')


