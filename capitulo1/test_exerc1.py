# teste do exercício 1
# arquivo de saída ou1.txt
# arquivo de entrada in1.txt
#
# Path: test_exerc1.py

import unittest
import sys
import os
from exerc1 import exerc1

def conta_linhas(arq):
    cont = 0
    for linha in arq:
        cont += 1
    return cont

class TestExerc1(unittest.TestCase):
    def setUp(self):
        # Configuração do ambiente de teste        
        # Abrir um arquivo temporário para escrita
        self.arq_tmp = open('temp.txt', "w+")

        # Abrir o arquivo de resposta
        self.arq_resposta = open("out1.txt", "r")
        
        # Redirecionar a saída para o arquivo temporário
        sys.stdout = self.arq_tmp

    def tearDown(self):
        # Finalização do ambiente de teste
        # Restaurar o stdout original (tela)
        sys.stdout = sys.__stdout__
        if self.arq_tmp:
         self.arq_tmp.close()
        if self.arq_resposta:
            self.arq_resposta.close()   
        os.remove('temp.txt')
    
    def test_tamanho(self):        
        exerc1()
        self.arq_tmp.seek(0)
        nl1 = conta_linhas(self.arq_tmp)
        nl2 = conta_linhas(self.arq_resposta)
        self.assertEqual(nl1, nl2, "Número de linhas diferente do esperado") 
        print("\nTeste de número de linhas OK", file=sys.stderr)

    def test_conteudo(self):
        exerc1()
        self.arq_tmp.seek(0)
        for linha in self.arq_resposta:
            self.assertEqual(linha, self.arq_tmp.readline(), "Conteúdo diferente do esperado")
        print("\nTeste de conteúdo OK", file=sys.stderr)

    def test_entrada_vazia(self):
        exerc1('vazio.txt')
        self.arq_tmp.seek(0)
        try:
            tamanho = self.arq_tmp.seek(0, os.SEEK_END)
            self.assertEqual(tamanho, 0, "Arquivo de saída não vazio")
        except FileNotFoundError:
            return False
        print("\nTeste de entrada vazia OK", file=sys.stderr)

    def test_milhao_linhas_tam(self):
        exerc1('milhao.txt')
        self.arq_tmp.seek(0)
        nl1 = conta_linhas(self.arq_tmp)
        nl2 = 1000000
        self.assertEqual(nl1, nl2, "Número de linhas diferente do esperado") 
        print("\nTeste de milhão de linhas OK", file=sys.stderr)

    def test_milhao_linhas_conteudo(self):
        exerc1('milhao.txt')
        self.arq_tmp.seek(0)
        self.arq_resposta.close()
        self.arq_resposta = open("milhaoResp1.txt", "r")
        for linha in self.arq_resposta:
            self.assertEqual(linha, self.arq_tmp.readline(), "Conteúdo diferente do esperado")
        print("\nTeste de milhão de linhas OK", file=sys.stderr)

if __name__ == '__main__':
    unittest.main()
    
