from datetime import datetime
from dateutil import relativedelta


class Aluno:
    def __init__(self, nome, data_de_nascimento, plano):
        self.__nome = nome
        self.__matriculado_em = self.hoje()
        self.__data_de_nascimento = data_de_nascimento
        self.__idade = self.__calcula_idade()
        self.__plano = plano
        print(f"Aluno {self.__nome} matriculado! Bem-vindo à PROBOXE!")

    @property
    def nome(self):
        return self.__nome

    @property
    def matriculado_em(self):
        return self.__matriculado_em

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento  # fazer um get_idade para calcular a idade baseado nessa data

    @property
    def idade(self):
        return self.__idade

    @property
    def plano(self):
        return self.__plano

    @plano.setter
    def plano(self, plano):
        plano_valido = plano in range(1, 6)
        if plano_valido:
            self.__plano = plano
        else:
            print("Insira um plano válido!")

    @matriculado_em.setter
    def matriculado_em(self, dia_da_matricula):
        self.__matriculado_em = dia_da_matricula

    def __calcula_idade(self):
        hoje = datetime.today()
        n_date = datetime.strptime(self.__data_de_nascimento, '%d/%m/%Y')
        idade = hoje.year - n_date.year - ((hoje.month, hoje.day) < (n_date.month, n_date.day))
        return idade

    @staticmethod
    def hoje():
        hoje = datetime.today()
        hoje_str = hoje.strftime('%d/%m/%Y')
        return hoje_str

    def __calcula_tempo_na_academia(self):
        hoje = datetime.today()
        matriculado = datetime.strptime(self.__matriculado_em, '%d/%m/%Y')
        diff = relativedelta.relativedelta(hoje, matriculado)
        anos = diff.years
        meses = diff.months
        dias = diff.days
        return anos, meses, dias

    def __tratamento_de_string(self):
        # Tratamento de string.
        global anos_str, meses_str, dias_str
        anos, meses, dias = self.__calcula_tempo_na_academia()
        if anos == 0:
            anos_str = ""
        elif anos == 1:
            if meses == 0 and dias == 0:
                anos_str = f"{anos} ano."
            elif meses != 0 and dias != 0:
                anos_str = f"{anos} ano,"
            else:
                anos_str = f"{anos} ano e"
        elif anos > 1:
            if meses == 0 and dias == 0:
                anos_str = f"{anos} anos."
            elif meses != 0 and dias != 0:
                anos_str = f"{anos} anos,"
            else:
                anos_str = f"{anos} anos e"
        if meses == 0:
            meses_str = ""
        elif meses == 1:
            if dias == 0:
                meses_str = f"{meses} mês."
            if dias > 0:
                meses_str = f"{meses} mês e"
        elif meses > 1:
            if dias == 0:
                meses_str = f"{meses} meses."
                dias_str = ""
            if dias > 0:
                meses_str = f"{meses} meses e"
        if dias == 0:
            dias_str = ""
        elif dias == 1:
            dias_str = f"{dias} dia."
        elif dias > 1:
            dias_str = f"{dias} dias."

    def imprime_tempo_na_academia(self):
        self.__tratamento_de_string()
        if not anos_str and not meses_str and not dias_str:
            print("Você se matriculou hoje!")
        else:
            tempo_na_academia = f"{anos_str} {meses_str} {dias_str}"
            print(' '.join(tempo_na_academia.split()))

    def imprime_dados(self):
        print(
            f"Aluno {self.__nome}, matriculado em {self.__matriculado_em}, {self.__idade} anos e treina {self.__plano} vezes na semana.")


"""
Linha de código básica p/ teste no console

from datetime import datetime
from dateutil import relativedelta
from aluno import Aluno
victor = Aluno('Victor', '29/08/1997', 5)
virginia = Aluno('Virginia', '19/06/1990', 5)
"""
