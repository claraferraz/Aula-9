import unittest
import e06


class MeuTeste(unittest.TestCase):
    def test_existe(self):
        t = 12
        valor = e06.tentativa(t)
        self.assertEqual(
            valor,
            [71, 33, 80, 72, 52, 41, 74, 31, 49, 40, 2, 61, 81, 43, 79, 45, 84, 42, 56],
        )

    def test_existe(self):
        t = 100
        valor = e06.tentativa(t)
        self.assertEqual(valor, "o número digitado não encontra-se no vetor")


if __name__ == "__main__":
    unittest.main()
