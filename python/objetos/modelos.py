from datetime import datetime
from dateutil import relativedelta

class Aluno:
    def __init__(self, nome, data_de_nascimento, plano):
        self._nome = nome.title()
        self._matriculado_em = self.hoje()
        self._data_de_nascimento = data_de_nascimento
        self._idade = self._calcula_idade()
        self._plano = plano
        self.bem_vindo()

    def bem_vindo(self):
        if str(type(self)) == "<class 'modelos.Aluno'>":
            print(f"Aluno {self._nome} matriculado! Bem-vindo à PROBOXE!")
        else:
            print(f"Atleta {self._nome} matriculado! Bem-vindo à PROBOXE!")

    @property
    def nome(self):
        return self._nome

    @property
    def matriculado_em(self):
        return self._matriculado_em

    @property
    def data_de_nascimento(self):
        return self._data_de_nascimento

    @property
    def idade(self):
        return self._idade

    @property
    def plano(self):
        return self._plano

    @plano.setter
    def plano(self, plano):
        plano_valido = plano in range(1, 6)
        if plano_valido:
            self.__plano = plano
        else:
            print("Insira um plano válido!")

    @matriculado_em.setter
    def matriculado_em(self, dia_da_matricula):
        self._matriculado_em = dia_da_matricula

    def _calcula_idade(self):
        """Método que calcula a idade baseado na data de nascimento do aluno."""
        hoje = datetime.today()
        n_date = datetime.strptime(self._data_de_nascimento, '%d/%m/%Y')
        idade = hoje.year - n_date.year - ((hoje.month, hoje.day) < (n_date.month, n_date.day))
        return idade

    @staticmethod
    def hoje():
        hoje = datetime.today()
        hoje_str = hoje.strftime('%d/%m/%Y')
        return hoje_str

    def _calcula_tempo_na_academia(self):
        hoje = datetime.today()
        matriculado = datetime.strptime(self._matriculado_em, '%d/%m/%Y')
        diff = relativedelta.relativedelta(hoje, matriculado)
        anos = diff.years
        meses = diff.months
        dias = diff.days
        return anos, meses, dias

    def _tratamento_de_string(self):
        # Tratamento de string.
        global anos_str, meses_str, dias_str
        anos, meses, dias = self._calcula_tempo_na_academia()
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
        self._tratamento_de_string()
        if not anos_str and not meses_str and not dias_str:
            print("Você se matriculou hoje!")
        else:
            tempo_na_academia = f"{anos_str} {meses_str} {dias_str}"
            print(' '.join(tempo_na_academia.split()))

    def __str__(self):
        return f"Aluno {self._nome}, matriculado em {self._matriculado_em}, {self._idade} anos e treina {self._plano} vezes na semana."


class Atleta(Aluno):

    def __init__(self, nome, data_de_nascimento, plano, peso):
        super().__init__(nome, data_de_nascimento, plano)
        self._peso = peso
        self._vitorias = 0
        self._derrotas = 0
        self._lutas = self._vitorias + self._derrotas
        self._categoria = self._calcula_categoria()

    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, novo_peso):
        self._peso = novo_peso

    @property
    def lutas(self):
        return f'{self._vitorias + self._derrotas} lutas. {self._vitorias} vitórias, {self._derrotas} derrotas.'
    
    @property
    def categoria(self):
        return self._categoria

    def vitoria(self):
        self._vitorias += 1
    
    def derrota(self):
        self._derrotas += 1

    def _calcula_categoria(self):
        if self._peso < 49:
            return 'mosca-ligeiro'
        elif self._peso < 52:
            return 'mosca'
        elif self._peso < 56:
            return 'galo'
        elif self._peso < 60:
            return 'leve'
        elif self._peso < 64:
            return 'médio-ligeiro'
        elif self._peso < 69:
            return 'meio-médio'
        elif self._peso < 75:
            return 'médio'
        elif self._peso < 81:
            return 'meio-pesado'
        elif self._peso < 92:
            return 'pesado'
        else:
            return 'super-pesado'
        
    def __str__(self):
        return f"Atleta {self._nome} que luta na categoria dos {self.categoria}s, matriculado em {self._matriculado_em}, {self._idade} anos, pesa {self._peso}kg e treina {self._plano} vezes na semana."
    
class Turma:
    
    def __init__(self, alunos):
        self._alunos = alunos

    def __getitem__(self, item):
        return self._alunos[item]
    
    def __len__(self):
        return len(self._alunos)