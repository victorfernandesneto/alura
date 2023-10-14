from datetime import datetime


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome.strip().title()
        self._data_nascimento = data_nascimento
        self._salario = salario
        self.decrescimo_salario()

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento = datetime.strptime(self._data_nascimento, '%d/%m/%Y')
        ano_atual = datetime.today()
        return ((ano_atual.year - data_nascimento.year) -
                ((ano_atual.month, ano_atual.day) < (data_nascimento.month, data_nascimento.day)))

    def sobrenome(self):
        nome_quebrado = self.nome.split()
        sobrenome = nome_quebrado[1:]
        return ' '.join(sobrenome)

    def _checa_diretor(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        sobrenomes_funcionario = self.sobrenome().split()
        for sobrenome in sobrenomes_funcionario:
            if sobrenome in sobrenomes:
                return True
        return False

    def decrescimo_salario(self):
        if self.salario > 100000 and self._checa_diretor():
            self._salario = round(self.salario * 0.9)
        return self.salario

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('Salário muito alto para bônus')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
