from Divisao import Divisao
from Multiplicacao import Multiplicacao
from Soma import Soma
from Subtracao import Subtracao
from Operacao import Operacao


class OperacaoFabrica():
    def criar(self, operador):
        if (operador == "soma"):
            return Soma()
        elif (operador == "subtracao"):
            return  Subtracao()
        elif(operador == "multiplicacao"):
            return Multiplicacao()
        elif(operador == "divisao"):
            return Divisao()
            
        