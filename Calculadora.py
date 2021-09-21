from OperacaoFabrica import OperacaoFabrica
from unittest import TestCase, main

class Calculadora():
    def calcular(self, valor1, valor2, operador):
        opFabrica = OperacaoFabrica()
        op = opFabrica.criar(operador)
        resultado = op.executar(valor1, valor2)
        return resultado
