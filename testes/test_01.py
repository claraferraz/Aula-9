import unittest
import e01


class MeuTeste(unittest.TestCase):
    def test_achei(self):
        valor = e01.tentativa("vasco")
        self.assertEqual(valor, "ACHEI")

    def test_nao_achei(self):
        valor = e01.tentativa("internacional")
        self.assertEqual(valor, "NÃO ACHEI")


if __name__ == "__main__":
    unittest.main()
