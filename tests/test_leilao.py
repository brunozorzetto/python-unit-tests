from unittest import TestCase
from src.leilao.dominio import Lance, Usuario, Leilao
from src.leilao.exceptions import LanceInvalido


class TestLeiao(TestCase):

    def setUp(self):
        """
        Este método já é invocado em cada método de teste

        :return: void
        """
        self.bruno = Usuario('Bruno', 10000.0)
        self.lance_bruno = Lance(self.bruno, 500.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):

        batman = Usuario('Batman', 10000.0)
        lance_batman = Lance(batman, 2000.0)

        self.leilao.propoe(self.lance_bruno)
        self.leilao.propoe(lance_batman)

        menor_valor_esperado = 500.0
        maior_valor_esperado = 2000.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            batman = Usuario('Batman', 10000.0)
            lance_batman = Lance(batman, 2000.0)

            self.leilao.propoe(lance_batman)
            self.leilao.propoe(self.lance_bruno)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):

        self.leilao.propoe(self.lance_bruno)

        self.assertEqual(500.0, self.leilao.menor_lance)
        self.assertEqual(500.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):

        batman = Usuario('Batman', 10000.0)
        lance_batman = Lance(batman, 2000.0)

        spider = Usuario('Spider', 10000.0)
        lance_spider = Lance(spider, 8000.0)

        self.leilao.propoe(self.lance_bruno)
        self.leilao.propoe(lance_batman)
        self.leilao.propoe(lance_spider)

        menor_valor_esperado = 500.0
        maior_valor_esperado = 8000.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):

        self.leilao.propoe(self.lance_bruno)

        quantidade_lances_recebida = len(self.leilao.lances)
        self.assertEqual(1, quantidade_lances_recebida)

    def test_deve_permitir_propror_um_lance_caso_o_ultimo_usuario_seja_diferente(self):

        spider = Usuario('Spider', 10000.0)
        lance_spider = Lance(spider, 600.0)

        self.leilao.propoe(self.lance_bruno)
        self.leilao.propoe(lance_spider)

        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):

        lance_do_bruno = Lance(self.bruno, 900.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_bruno)
            self.leilao.propoe(lance_do_bruno)

