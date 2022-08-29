import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connetion = conexao()
        self.db_connetion = self.db_connetion.conectar()
        self.com = self.db_connetion.cursor()

    def inserir(self, nome, endereco, telefone, dataDeNascimento):
        try:
            sql = "insert into pessoa(codigo, nome, edereco, telefone, datadeNascimento) values('', '{}', '{}', '{}', '{}')".format(nome, endereco, telefone, dataDeNascimento)
            self.con.execute(sql)
            self.db_connetion.commit()
            return "{} linhas afetadas".format(self.com.rowcount)
        except Exception as erro:
            return erro

    def selecionar(self):
        try:
            sql = "select * from pessoa"
            self.con.execute(sql)
            msg = ""
            for(codigo, nome, endereco ,telefone , dataDeNascimento)
                msg = msg +"\ncodigo: {}, nome: {}, endereço: {}, telefone: {}, Data de nascimento: {}".format(codigo, nome, endereco, telefone, dataDeNascimento)
            return msg

        except Exception as erro:
            erro
