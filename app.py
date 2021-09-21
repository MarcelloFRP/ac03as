from unittest import TestCase, main
from Calculadora import Calculadora

class Testes(TestCase):
    def test_soma(self):
        calculadora = Calculadora()
        result = calculadora.calcular(2, 3, "soma")
        self.assertEqual(result, 5)
    
    def test_subtracao(self):
        calculadora = Calculadora()
        result = calculadora.calcular(5, 3, "subtracao")
        self.assertEqual(result, 2)
    
    def test_multiplicacao(self):
        calculadora = Calculadora()
        result = calculadora.calcular(5, 3, "multiplicacao")
        self.assertEqual(result, 15)
    
    def test_divisao(self):
        calculadora = Calculadora()
        result = calculadora.calcular(15, 3, "divisao")
        self.assertEqual(result, 5)



if __name__ == '__main__':
    main()