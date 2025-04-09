# teste do exercício 8
# arquivo de saída ou8.txt
# arquivo de entrada in8.txt
# Path: test_exerc8.py

import unittest
import sys
import os
from exerc8 import exerc8

def conta_linhas(arq):
    cont = 0
    for linha in arq:
        cont += 1
    return cont

class TestExerc(unittest.TestCase):
    def setUp(self):
        # Configuração do ambiente de teste
        self.arq_out = open("temp.txt", "w+")
        self.arq_resposta = open("out8.txt", "r")
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
        exerc8()
        self.arq_out.close() # fecha o arquivo de saída do programa
        self.arq_out = open("temp.txt", "r")
        nl1 = conta_linhas(self.arq_out)
        nl2 = conta_linhas(self.arq_resposta)
        self.assertEqual(nl1, nl2, "Número de linhas diferente do esperado") 
        print("\nTeste de número de linhas OK", file=sys.stderr)

    def test_conteudo(self):
        exerc8()
        self.arq_out.close()
        self.arq_out = open("temp.txt", "r")
        for linha in self.arq_resposta:
            self.assertEqual(linha.strip(), self.arq_out.readline().strip(), "Conteúdo diferente do esperado")
        print("\nTeste de conteúdo OK", file=sys.stderr)

    def test_entrada_vazia(self):
        exerc8('vazio.txt')
        try:
            tamanho = os.path.getsize('temp.txt')
            self.assertEqual(tamanho, 0, "Arquivo de saída não vazio")
        except FileNotFoundError:
            print("Arquivo de saída não encontrado", file=sys.stderr)
            return
        print("\nTeste de entrada vazia OK", file=sys.stderr)

    def test_milhao(self):
        exerc8('milhao.txt')
        self.arq_out.seek(0) # reposiciona o ponteiro do arquivo de saída
        self.arq_resposta.close()
        self.arq_resposta = open("milhaoParImpar.txt", "r")
        for linha in self.arq_resposta:
            self.assertEqual(linha.strip(), self.arq_out.readline().strip(), 
                             "Conteúdo diferente do esperado")
        print("\nTeste de conteúdo de um milhão de linhas OK", file=sys.stderr)

if __name__ == '__main__':
    unittest.main()
    
