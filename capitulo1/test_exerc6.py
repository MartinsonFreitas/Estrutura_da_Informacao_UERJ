# teste do exercício 6
# arquivo de saída ou6.txt
# arquivo de entrada in6.txt
# Path: test_exerc6.py

import unittest
import sys
import os
from exerc6 import exerc6

def conta_linhas(arq):
    cont = 0
    for linha in arq:
        cont += 1
    return cont

class TestExerc(unittest.TestCase):
    def setUp(self):
        # Configuração do ambiente de teste
        self.arq_out = open("temp.txt", "w")
        self.arq_resposta = open("out6.txt", "r")
        sys.stdout = self.arq_out

    def tearDown(self):
        # Finalização do ambiente de teste
        sys.stdout = sys.__stdout__
        if self.arq_out:
            self.arq_out.close()
        if self.arq_resposta:
            self.arq_resposta.close()
        os.remove("temp.txt")
    
    def test_tamanho(self):        
        exerc6()
        self.arq_out.close() # fecha o arquivo de saída do programa
        self.arq_out = open("temp.txt", "r")
        nl1 = conta_linhas(self.arq_out)
        nl2 = conta_linhas(self.arq_resposta)
        self.assertEqual(nl1, nl2, "Número de linhas diferente do esperado") 
        print("\nTeste de número de linhas OK", file=sys.stderr)

    def test_conteudo(self):
        exerc6()
        self.arq_out.close()
        self.arq_out = open("temp.txt", "r")
        for linha in self.arq_resposta:
            self.assertEqual(linha.strip(), self.arq_out.readline().strip(), "Conteúdo diferente do esperado")
        print("\nTeste de conteúdo OK", file=sys.stderr)

if __name__ == '__main__':
    unittest.main()
    
