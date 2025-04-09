# teste do exercício 9
# arquivo de entrada in9.txt
# Path: test_exerc9.py

import unittest
import sys
import os
from exerc9 import exerc9

def conta_linhas(arq):
    cont = 0
    for linha in arq:
        cont += 1
    return cont

class TestExerc(unittest.TestCase):
    def setUp(self):
        # Configuração do ambiente de teste
        self.arq_out = open("temp.txt", "w+")
        sys.stdout = self.arq_out

    def tearDown(self):
        # Finalização do ambiente de teste
        sys.stdout = sys.__stdout__
        if self.arq_out:
            self.arq_out.close()
        os.remove("temp.txt")

    def test_tamanho(self):
        exerc9()
        self.arq_out.seek(0) # reposiciona o ponteiro do arquivo de saída
        nl1 = conta_linhas(self.arq_out)
        nome_arq = "in9.txt"
        arq = open(nome_arq, "r")
        nl2 = conta_linhas(arq)
        arq.close()
        self.assertEqual(nl1, nl2, "Número de linhas diferente do esperado")
        print("\nTeste de número de linhas OK", file=sys.stderr)

    def test_milhao_tam(self):
        exerc9('milhao.txt')
        self.arq_out.close()
        self.arq_out = open("temp.txt", "r")
        nl1 = conta_linhas(self.arq_out)
        self.assertEqual(nl1, 1000000, "Número de linhas diferente do esperado")
        print("\nTeste de número de linhas OK", file=sys.stderr)

if __name__ == '__main__':
    unittest.main()
        
