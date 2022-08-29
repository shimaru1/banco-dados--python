import mysql.connector  # Elenento que faz a conexão com o banco de dados
from mysql.connector import errorcode


class conexao:
    def __init__(self):
        pass

    def conectar(self):
        try:

            self.db_connection = mysql.connector.connect(host='localhost', user='root', password='',
                                                         database='bdTi14TPython')

            print('Conectado com sucesso!')
            return self.db_connection
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR:  # Caso não exista um banco de dados!
                print('Banco de dados não existe! \n Erro: {}'.format(erro))
            elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:  # Há um erro de usuario
                print('nome de usuario ou senha invalida! \n erro:{}'.format(erro))
            else:
                print(erro)
        else:
            self.db_connection.close()  # Fechando a conexão com o banco de dados
