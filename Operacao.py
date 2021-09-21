import abc

class Operacao(metaclass=abc.ABCMeta):
    def executar(self, valor1, valor2):
        pass