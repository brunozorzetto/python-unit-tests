from unittest import TestCase
from src.leilao.dominio import Lance, Usuario, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_avalia(self):
        bruno = Usuario('Bruno')
        batman = Usuario('Batman')

        lance_batman = Lance(batman, 2000.0)
        lance_bruno = Lance(bruno, 500.0)

        leilao = Leilao('Celular')
        leilao.lances.append(lance_bruno)
        leilao.lances.append(lance_batman)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 500.0
        maior_valor_esperado = 2000.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
