# teste do exercício 2
# arquivo de saída ou2.txt
# arquivo de entrada in2.txt
# Path: test_exerc2.py

import unittest
import sys
import os
from exerc2 import exerc2

def conta_linhas(arq):
    arq.seek(0)
    cont = 0
    for linha in arq:
        cont += 1
    return cont

class TestExerc2(unittest.TestCase):
    def setUp(self):
        # Configuração do ambiente de teste
        self.arq_out = open("temp.txt", "w+")
        self.arq_resposta = open("out2.txt", "r")
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
        exerc2()
        self.arq_out.seek(0) # reposiciona o ponteiro do arquivo de saída   
        nl1 = conta_linhas(self.arq_out)
        nl_resposta = conta_linhas(self.arq_resposta)
        self.assertEqual(nl1, nl_resposta, "Número de linhas diferente do esperado") 
        print("\nTeste de número de linhas OK", file=sys.stderr)

    def test_conteudo(self):
        exerc2()
        self.arq_out.seek(0) # reposiciona o ponteiro do arquivo de saída
        for linha in self.arq_resposta:
            self.assertEqual(linha, self.arq_out.readline(), "Conteúdo diferente do esperado")
        print("\nTeste de conteúdo OK", file=sys.stderr)

    def test_entrada_vazia(self):
        exerc2('vazio.txt')
        try:
            tamanho = os.path.getsize('temp.txt')
            self.assertEqual(tamanho, 0, "Arquivo de saída não vazio")
        except FileNotFoundError:
            print("Arquivo de saída não encontrado", file=sys.stderr)
            return
        print("\nTeste de entrada vazia OK", file=sys.stderr)
        
    def test_entrada_menor_50(self):
        exerc2('trintaLinhas.txt')
        arq_resposta = open("trintaLinhasResp.txt", "r")
        nl1 = conta_linhas(self.arq_out)
        nl_resposta = conta_linhas(arq_resposta)
        arq_resposta.close()
        self.assertEqual(nl1, nl_resposta, "Número de linhas diferente do esperado") 
        print("\nTeste de número de linhas menos de 50 linhas OK", file=sys.stderr)

    def test_entrada_conteudo_menor_50(self):
        exerc2('trintaLinhas.txt')
        arq_resposta = open("trintaLinhasResp.txt", "r")
        self.arq_out.seek(0)
        for linha in arq_resposta:
            self.assertEqual(linha, self.arq_out.readline(), "Conteúdo diferente do esperado")
        arq_resposta.close()
        print("\nTeste de conteúdo menos de 50 linhas OK", file=sys.stderr)

    def test_milhao_linhas_tam(self):
        exerc2('milhao.txt')
        self.arq_out.seek(0)
        nl1 = conta_linhas(self.arq_out)
        nl2 = 1000000
        self.assertEqual(nl1, nl2, "Número de linhas diferente do esperado") 
        print("\nTeste de tamanho milhão de linhas OK", file=sys.stderr)

    def test_milhao_linhas_conteudo(self):
        exerc2('milhao.txt')
        self.arq_out.seek(0)
        self.arq_resposta.close()
        self.arq_resposta = open("milhaoResp2.txt", "r")
        for linha in self.arq_resposta:
            self.assertEqual(linha, self.arq_out.readline(), "Conteúdo diferente do esperado")
        print("\nTeste de conteúdo milhão de linhas OK", file=sys.stderr)

if __name__ == '__main__':
    unittest.main()
    
