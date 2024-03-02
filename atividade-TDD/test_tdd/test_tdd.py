import unittest
from  src.determinarAprovacao import  determinarAprovação

class test_TDD(unittest.TestCase):
    def test_aprovado_geral(self):
        expected = "aprovado"
        actual = determinarAprovação(100, 100, 100)
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message

    def test_aprovado_frequencia_reprovado_geral(self):
        expected = "reprovado"
        actual = determinarAprovação(100, 30, 30)
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message

    def test_aprovado_notas_reprovado_frequencia(self):
        expected = "reprovado"
        actual = determinarAprovação(74, 60, 60)
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message

    def test_aprovado_nota_especial(self):
        expected = "aprovado"
        actual = determinarAprovação(75, 60, 100)
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message

    def test_reprovado_nota_especial(self):
        expected = "reprovado"
        actual = determinarAprovação(75, 60, 0)
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message

    def test_reprovado_nota_geral(self):
        expected = "reprovado"
        actual = determinarAprovação(75, 0, 60)
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message

    def test_numeros_negativos(self):
        expected = "reprovado"
        actual = determinarAprovação(-1, -1, -1)
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message
    
    def test_unico_numero_negativo(self):
        expected = "reprovado"
        actual = determinarAprovação(75, 100, -1)
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message


