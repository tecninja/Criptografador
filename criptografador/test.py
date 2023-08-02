import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from main import Codificador
from unittest import TestCase


class TestCodificador(TestCase):

    def test_md5(self):
        
        esperado = "698dc19d489c4e4db73e28a713eab07b"
        resultado = Codificador().md5('teste')
        
        assert esperado == resultado, "Erro na criptografia MD5"
        
    def test_criptografia(self):
        
        palavra = "Teste"
        key = b'mW4YEyV-XytAXO9g4ZpQP2PizkH4HE5m54ZkQus3gJg='
        
        criptografia = Codificador().criptografia(palavra, key)
        descriptografia = Codificador().descriptografia(criptografia, key).decode()
        
        assert palavra == descriptografia, "Erro na criptografia"
