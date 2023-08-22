from codigo.bytebank import Funcionario
from datetime import date
import pytest
from pytest import mark


class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_pass(self):
        #Given-Contexto
        entrada = '13/03/2000'
        esperado = date.today().year - 2000

        #When-ação
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        #Then-desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(
            self):
        #Given
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'

        #When
        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()

        #Then
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        #given
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        # when
        funconario_teste = Funcionario(entrada_nome, '11/11/2000',
                                       entrada_salario)
        funconario_teste.decrescimo_salario()
        resultado = funconario_teste.salario

        # then
        assert resultado == esperado
        
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # given
        entrada = 1000
        esperado = 100

        # when
        funconario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funconario_teste.calcular_bonus()

        # then
        assert resultado == esperado
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(
            self):
        # given
        with pytest.raises(Exception):
            entrada = 100000000  
            
            # when
            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()  
            
            # then
            assert resultado  
