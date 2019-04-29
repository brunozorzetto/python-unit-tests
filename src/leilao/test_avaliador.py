from unittest import TestCase
from src.leilao.dominio import Lance, Usuario, Leilao


class TestAvaliador(TestCase):

    def setUp(self):
        """
        Este método já é invocado em cada método de teste

        :return: void
        """
        self.bruno = Usuario('Bruno')
        self.lance_bruno = Lance(self.bruno, 500.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):

        batman = Usuario('Batman')
        lance_batman = Lance(batman, 2000.0)

        self.leilao.propoe(self.lance_bruno)
        self.leilao.propoe(lance_batman)

        menor_valor_esperado = 500.0
        maior_valor_esperado = 2000.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):

        batman = Usuario('Batman')
        lance_batman = Lance(batman, 2000.0)

        self.leilao.propoe(lance_batman)
        self.leilao.propoe(self.lance_bruno)

        menor_valor_esperado = 500.0
        maior_valor_esperado = 2000.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):

        self.leilao.propoe(self.lance_bruno)

        self.assertEqual(500.0, self.leilao.menor_lance)
        self.assertEqual(500.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):

        batman = Usuario('Batman')
        lance_batman = Lance(batman, 2000.0)

        spider = Usuario('Spider')
        lance_spider = Lance(spider, 8000.0)

        self.leilao.propoe(lance_batman)
        self.leilao.propoe(self.lance_bruno)
        self.leilao.propoe(lance_spider)

        menor_valor_esperado = 500.0
        maior_valor_esperado = 8000.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

