from Operacao import Operacao


class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado