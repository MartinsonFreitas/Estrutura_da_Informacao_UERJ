# teste do exercício 5
# arquivo de saída ou5.txt
# arquivo de entrada in5.txt
# Path: test_exerc5.py

import unittest
import sys
import os
from exerc5 import exerc5

def conta_linhas(arq):
    cont = 0
    for linha in arq:
        cont += 1
    return cont

class TestExerc(unittest.TestCase):
    def setUp(self):
        # Configuração do ambiente de teste
        self.arq_out = open("temp.txt", "w+")
        self.arq_resposta = open("out5.txt", "r")
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
        exerc5()
        self.arq_out.close() # fecha o arquivo de saída do programa
        self.arq_out = open("temp.txt", "r")
        nl1 = conta_linhas(self.arq_out)
        nl2 = conta_linhas(self.arq_resposta)
        self.assertEqual(nl1, nl2, "Número de linhas diferente do esperado") 
        print("\nTeste de número de linhas OK", file=sys.stderr)

    def test_conteudo(self):
        exerc5()
        self.arq_out.close()
        self.arq_out = open("temp.txt", "r")
        for linha in self.arq_resposta:
            self.assertEqual(linha.strip(), self.arq_out.readline().strip(), "Conteúdo diferente do esperado")
        print("\nTeste de conteúdo OK", file=sys.stderr)

    def test_entrada_vazia(self):
        exerc5('vazio.txt')
        try:
            tamanho = os.path.getsize('temp.txt')
            self.assertEqual(tamanho, 0, "Arquivo de saída não vazio")
        except FileNotFoundError:
            print("Arquivo de saída não encontrado", file=sys.stderr)
            return
        print("\nTeste de entrada vazia OK", file=sys.stderr)

    def test_milhao(self):
        exerc5('milhaoRepetidas.txt')
        self.arq_out.seek(0)
        self.arq_resposta.close()
        self.arq_resposta = open("milhaoRepetidasResp.txt", "r")
        nl1 = conta_linhas(self.arq_out)
        nl2 = conta_linhas(self.arq_resposta)
        self.assertEqual(nl1, nl2, "Número de linhas diferente do esperado") 
        print("\nTeste de número de linhas OK", file=sys.stderr)
        self.arq_out.seek(0)
        self.arq_resposta.seek(0)
        for linha in self.arq_resposta:
            self.assertEqual(linha.strip(), self.arq_out.readline().strip(), "Conteúdo diferente do esperado")
        print("\nTeste de conteúdo OK", file=sys.stderr)

    def test_milhao_tam(self):
        exerc5('milhaoRepetidas.txt')
        self.arq_out.seek(0)
        nl1 = conta_linhas(self.arq_out)
        nl2 = 999000
        self.assertEqual(nl1, nl2, "Número de linhas diferente do esperado") 
        print("\nTeste de arquivo milhão de linhas número de linhas OK", file=sys.stderr)

if __name__ == '__main__':
    unittest.main()
    
