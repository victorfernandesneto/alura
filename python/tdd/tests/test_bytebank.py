from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    @mark.idade
    def test_data_de_nascimento_29_08_1997_retorna_26(self):
        entrada = '29/08/1997'  # Given
        saida = 26
        funcionario_teste = Funcionario('Aleatório', entrada, 1111)

        resultado = funcionario_teste.idade()  # When

        assert resultado == saida  # Then

    @mark.sobrenome
    def test_dois_nomes_retorna_um_sobrenome(self):
        entrada = 'Victor Fernandes'  # Given
        saida = 'Fernandes'
        funcionario_teste = Funcionario(entrada, '29/08/1997', 1111)

        resultado = funcionario_teste.sobrenome()  # When

        assert resultado == saida

    @mark.sobrenome
    def test_tres_nomes_retorna_dois_sobrenomes(self):
        entrada = 'Victor Fernandes Neto'  # Given
        saida = 'Fernandes Neto'
        funcionario_teste = Funcionario(entrada, '29/08/1997', 1111)

        resultado = funcionario_teste.sobrenome()  # When

        assert resultado == saida

    @mark.sobrenome
    def test_um_nome_retorna_nenhum_sobrenome(self):
        entrada = 'Victor'  # Given
        saida = ''
        funcionario_teste = Funcionario(entrada, '29/08/1997', 1111)

        resultado = funcionario_teste.sobrenome()  # When

        assert resultado == saida

    @mark.decrescimo
    def test_diretor_com_salario_maior_que_100000_retorna_salario_reduzido(self):
        entrada = 100001
        saida = round(100001 * 0.9)
        diretor_teste = Funcionario('paula bragança paulista', '01/01/1901', entrada)

        resultado = diretor_teste.salario

        assert resultado == saida

    @mark.decrescimo
    def test_diretor_com_salario_menor_que_100000_retorna_salario_nao_reduzido(self):
        entrada = 28557
        saida = entrada
        funcionario_teste = Funcionario('Zaffari Bourbon', '29/08/1997', entrada)

        resultado = funcionario_teste.salario

        assert resultado == saida

    @mark.decrescimo
    def test_funcionario_com_salario_maior_que_100000_retorna_salario_nao_reduzido(self):
        entrada = 203489
        saida = entrada
        diretor_teste = Funcionario('Funcionário brabo', '29/08/1997', entrada)

        resultado = diretor_teste.salario

        assert resultado == saida

    @mark.calcular_bonus
    def test_bonus_de_salario_de_9999_retorna_999(self):
        entrada = 9999
        saida = 9999*0.1
        funcionario_teste = Funcionario('Victor', '29/08/1997', entrada)

        resultado = funcionario_teste.calcular_bonus()

        assert resultado == saida

    @mark.calcular_bonus
    def test_bonus_de_salario_de_99999_retorna_exception(self):
        with pytest.raises(Exception):  # funciona como a variável 'saída' anterior
            entrada = 99999
            funcionario_teste = Funcionario('Victor', '29/08/1997', entrada)

            funcionario_teste.calcular_bonus()