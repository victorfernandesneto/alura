from datetime import datetime
class Aluno:
    def __init__(self, nome, matriculado_em, nascimento, plano):
        self.__nome               = nome
        self.__matricula          = matriculado_em
        self.__data_de_nascimento = nascimento
        self.__plano              = plano
        print(f"Aluno {self.__nome} matriculado! Bem-vindo à PROBOXE!")

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento # fazer um get_idade para calcular a idade baseado nessa data

    def idade(self):
        hoje = datetime.today()
        nascimento = datetime.strptime(self.__data_de_nascimento, '%d/%m/%Y') # Essa linha só é necessária pois a data de nascimento está sendo inserida como string.
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade


    def tempo_na_academia(self):
        hoje = datetime.today()
        matriculado = datetime.strptime(self.__matriculado_em, '%d/%m/%Y') # Essa linha só é necessária pois a data de matrícula está sendo inserida como string.
        tempo = hoje.year - matriculado.year - ((hoje.month, hoje.day) < (matriculado.month, matriculado.day))
        return tempo

    @property
    def plano(self):
        return self.__plano

    @plano.setter
    def plano(self, plano):
        plano_invalido = plano > 5 or plano < 1
        if(plano_invalido):
            print("Insira um plano válido!")
        else:
            self.__plano = plano

    def imprime_dados(self):
        print(f"Aluno {self.__nome}, matriculado em {self.__matricula}, {self.idade()} anos e treina {self.__plano} vezes na semana.")

"""
Linha de código básica p/ teste no console

from datetime import datetime
from aluno import Aluno
victor = Aluno('Victor', '12/12/2012', '29/08/1997', 5)
virginia = Aluno('Virginia', '12/12/2012', '19/06/1990', 5)
"""