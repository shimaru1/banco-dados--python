from model import model

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()


    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print('\n\nEscolha uma das opções abaixo: ' +
              '\n0. Sair' +
              '\n1. Cadastrar' +
              '\n2. Consultar' +
              '\n4. Atualizar' +
              '\n5. Excluir')
        self.setOpcao(int(input()))

    def cadastrar(self):
        print("informe o seu nome: ")
        nome = input()
        print("informe o seu  endereço: ")
        endereco = input()
        print("informe o seu telefone: ")
        telefone = input()
        print("informe o sua data de nascimento: ")
        dataDeNascimento = input()
        print(self.modelo.inserir(nome, endereco, telefone, self.transformarData(dataDeNascimento)))

    def transformarData(self, texto):
        separado = texto.split('/')
        dia = separado[0]
        mes = separado[0]
        ano = separado[0]
        return "{}-{}{}".format(ano, mes, dia)


    def operacoes(self):
        while self.getOpcao() !=0:
            self.menu()
            if self.getOpcao() == 0:
                print("obrigado!")
            elif self.getOpcao() == 1:
                self.cadastrar()
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            else:
                print("opção escolhida invalida! \ntenta novamente!")