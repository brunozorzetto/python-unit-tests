import pytest
from src.leilao.dominio import Usuario, Leilao
from src.leilao.exceptions import LanceInvalido


@pytest.fixture
def bruno():
    return Usuario('Bruno', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(bruno, leilao):

    bruno.propoe_lance(leilao, 50.0)

    assert (bruno.carteira == 50.0)

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(bruno, leilao):

    bruno.propoe_lance(leilao, 1.0)

    assert (bruno.carteira == 99.0)

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(bruno, leilao):

    bruno.propoe_lance(leilao, 100.0)

    assert (bruno.carteira == 0.0)

def test_deve_permitir_propor_lance_quando_o_valor_eh_maior_que_o_valor_da_carteira(bruno, leilao):

    with pytest.raises(LanceInvalido):

        bruno.propoe_lance(leilao, 200.0)
