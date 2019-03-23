import unittest
import Anagrams

class TestAnagramas(unittest.TestCase):

    def test_resultado(self):
        palabras = open('wordlist.txt')
        numero_conjuntos_anagramas = Anagrams.contar_conjuntos_anagramas(palabras)
        palabras.close()
        
        self.assertEqual(numero_conjuntos_anagramas, 20683)

if __name__ == '__main__':
    unittest.main() 
