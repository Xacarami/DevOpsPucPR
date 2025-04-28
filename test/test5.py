from unittest.mock import patch
from src.aula5 import *

def gerar_numero_secreto():
    with patch('random.randint', return_value=5):
        result = gerar_numero_secreto()
        assert result == 5

def test_verificar_palpite_acerto():
    verificando_palpite_certo = verificar_palpite(5, 5)
    assert verificando_palpite_certo

def test_verificar_palpite_erro():
    verificando_palpite_errado = verificar_palpite(5, 3)
    assert not verificando_palpite_errado

