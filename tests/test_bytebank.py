import pytest
from pytest import mark

from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13032000_deve_retornar_22(self):
        entrada = "13/03/2000"  # Given
        esperado = 22

        funcionario_teste = Funcionario("Teste", entrada, 5000)

        resultado = funcionario_teste.idade()  # When

        assert resultado == esperado  # Then

    def test_quando_nome_recebe_lucas_carvalho_retorna_carvalho(self):
        entrada = "Lucas Carvalho"
        esperado = "Carvalho"
        lucas = Funcionario(entrada, "11/11/2000", 1600)
        resultado = lucas.sobrenome()
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_retorna_90000(self):
        entrada_salario = 100000
        entrada_nome = "Paulo Silva"
        esperado = 90000
        funcionario_teste = Funcionario(entrada_nome, "11/11/2000", entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_retornar_100(self):
        entrada_salario = 1000
        esperado = 100
        funcionario_teste = Funcionario("Teste", "11/11/2000", entrada_salario)
        resultado = funcionario_teste.calcular_bonus()
        assert resultado == esperado
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 100000
            funcionario_teste = Funcionario("Teste", "11/11/2000", entrada_salario)
            resultado = funcionario_teste.calcular_bonus()
            assert resultado

    def test_retorno_str(self):
        nome, data_nascimento, salario = "Teste", "05/05/1989", 1600
        esperado = "Funcionario(Teste, 05/05/1989, 1600)"
        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()
        assert resultado == esperado