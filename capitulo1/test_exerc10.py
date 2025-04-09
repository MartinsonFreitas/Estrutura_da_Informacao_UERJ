# teste do exercício 10
# Path: test_exerc8.py

import unittest
import sys
import os
from exerc10 import exerc10

class TestExerc(unittest.TestCase):
    def test_01(self):
        self.assertTrue(exerc10("{{()[]}}"), "É uma string casada, mas retornou False")

    def test_02(self):
        self.assertFalse(exerc10("{{()[]"), "Não é uma string casada, mas retornou True")

    def test_03(self):
        self.assertFalse(exerc10("{{()[]}}{"), "Não é uma string casada, mas retornou True")

    def test_04(self):
        self.assertTrue(exerc10("{{()[]}}{}"), "É uma string casada, mas retornou False")

    def test_05(self):
        self.assertFalse(exerc10("{{()[]}}{}{"), "Não é uma string casada, mas retornou True")

    def test_06(self):
        self.assertTrue(exerc10(""), "É uma string casada, mas retornou False")

    def test_07(self):
        self.assertTrue(exerc10("{{()[]}}"), "É uma string casada, mas retornou False")

    def test_08(self):
        self.assertFalse(exerc10("{{()[]}"), "Não é uma string casada, mas retornou True")

    def test_09(self):
        self.assertFalse(exerc10("{{()]}"), "Não é uma string casada, mas retornou True")

    def test_10(self):
        self.assertFalse(exerc10("{{()[]}}{"), "Não é uma string casada, mas retornou True")

    def test_11(self):
        self.assertTrue(exerc10("{{()[]}}{}"), "É uma string casada, mas retornou False")

    def test_12(self):
        self.assertFalse(exerc10("{{()[]}}{}{"), "Não é uma string casada, mas retornou True")

    def test_13(self):
        self.assertTrue(exerc10("{{()[]}}{}{}"), "É uma string casada, mas retornou False")

    def test_14(self):
        self.assertFalse(exerc10("{{()[]}}{}{}{"), "Não é uma string casada, mas retornou True")

    def test_15(self):
        self.assertTrue(exerc10("{{()[]}}{}{}{}"), "É uma string casada, mas retornou False")

    def test_16(self):
        self.assertFalse(exerc10("{{()[]}}{}{}{}{"), "Não é uma string casada, mas retornou True")

    def test_17(self):
        self.assertTrue(exerc10("{{()[]}}{}{}{}{}"), "É uma string casada, mas retornou False")

    def test_18(self):
        self.assertFalse(exerc10("{]"), "Não é uma string casada, mas retornou True")

    def test_19(self):
        self.assertTrue(exerc10("{{()[]}}{}{}{}{}{}[]"), "É uma string casada, mas retornou False")

    def test_20(self):
        self.assertRaises(IndexError, exerc10,"{{()[]}}{}{}{}{}{}[]]")   

if __name__ == '__main__':
    unittest.main()   
    